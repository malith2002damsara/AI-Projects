import os
import PyPDF2
import pdfplumber
from typing import List, Dict, Any, Optional
from logger import setup_logger

logger = setup_logger(__name__)


class SimplePDFLoader:
    """PDF loader supporting multiple backends (PyPDF2 and pdfplumber)"""
    
    def __init__(self, file_path: str, backend: str = "pypdf2"):
        self.file_path = file_path
        self.backend = backend
        self.documents = []

    def load_with_pypdf2(self) -> List[Dict[str, Any]]:
        """Load PDF using PyPDF2 backend"""
        documents = []
        try:
            with open(self.file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                total_pages = len(pdf_reader.pages)
                
                for page_num, page in enumerate(pdf_reader.pages):
                    try:
                        text = page.extract_text()
                        if text and text.strip():
                            documents.append({
                                "page_content": text,
                                "metadata": {
                                    "source": self.file_path,
                                    "filename": os.path.basename(self.file_path),
                                    "page": page_num + 1,
                                    "total_pages": total_pages
                                }
                            })
                    except Exception as e:
                        logger.warning(f"Failed to extract page {page_num + 1}: {e}")
                        continue
                        
        except FileNotFoundError:
            logger.error(f"PDF file not found: {self.file_path}")
            raise
        except PyPDF2.errors.PdfReadError as e:
            logger.error(f"[PyPDF2] Corrupted PDF file {os.path.basename(self.file_path)}: {e}")
        except Exception as e:
            logger.error(f"[PyPDF2] Error loading {os.path.basename(self.file_path)}: {e}")
        
        return documents

    def load_with_pdfplumber(self) -> List[Dict[str, Any]]:
        """Load PDF using pdfplumber backend"""
        documents = []
        try:
            with pdfplumber.open(self.file_path) as pdf:
                total_pages = len(pdf.pages)
                
                for page_num, page in enumerate(pdf.pages):
                    try:
                        text = page.extract_text()
                        if text and text.strip():
                            documents.append({
                                "page_content": text,
                                "metadata": {
                                    "source": self.file_path,
                                    "filename": os.path.basename(self.file_path),
                                    "page": page_num + 1,
                                    "total_pages": total_pages
                                }
                            })
                    except Exception as e:
                        logger.warning(f"Failed to extract page {page_num + 1}: {e}")
                        continue
                        
        except FileNotFoundError:
            logger.error(f"PDF file not found: {self.file_path}")
            raise
        except Exception as e:
            logger.error(f"[pdfplumber] Error loading {os.path.basename(self.file_path)}: {e}")
        
        return documents

    def load(self) -> List[Dict[str, Any]]:
        """Load PDF with the configured backend"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"PDF file not found: {self.file_path}")
        
        if self.backend == "pypdf2":
            self.documents = self.load_with_pypdf2()
        elif self.backend == "pdfplumber":
            self.documents = self.load_with_pdfplumber()
        else:
            logger.error(f"Unknown backend: {self.backend}")
            raise ValueError(f"Unsupported backend: {self.backend}. Use 'pypdf2' or 'pdfplumber'.")
        return self.documents


class RAGPDFDirectoryLoader:
    """Load all PDFs from a directory recursively"""
    
    def __init__(self, folder_path: str):
        self.folder_path = folder_path
        self.all_documents: List[Dict[str, Any]] = []
        self.failed_files: List[str] = []
        self.loaded_files: List[str] = []

    def discover_pdfs(self) -> List[str]:
        """Discover all PDF files in the directory tree"""
        pdf_files = []
        try:
            for root, dirs, files in os.walk(self.folder_path):
                for file in sorted(files):
                    if file.lower().endswith(".pdf"):
                        pdf_files.append(os.path.join(root, file))
        except Exception as e:
            logger.error(f"Error discovering PDFs in {self.folder_path}: {e}")
        
        return pdf_files

    def load_single_pdf(self, pdf_path: str) -> List[Dict[str, Any]]:
        """Load a single PDF with fallback to alternative backend"""
        loader = SimplePDFLoader(pdf_path, backend="pypdf2")
        docs = loader.load()
        
        if not docs:
            logger.debug(f"PyPDF2 returned empty, retrying with pdfplumber...")
            loader = SimplePDFLoader(pdf_path, backend="pdfplumber")
            docs = loader.load()
        
        return docs

    def load_all(self) -> List[Dict[str, Any]]:
        """Load all PDFs from the directory"""
        if not os.path.exists(self.folder_path):
            logger.error(f"PDF folder not found: {self.folder_path}")
            raise FileNotFoundError(f"PDF folder not found: {self.folder_path}")

        pdf_files = self.discover_pdfs()
        
        if not pdf_files:
            logger.warning(f"No PDF files found in: {self.folder_path}")
            return []

        logger.info(f"Found {len(pdf_files)} PDF(s) in '{self.folder_path}'")

        for i, pdf_path in enumerate(pdf_files, 1):
            filename = os.path.basename(pdf_path)
            logger.info(f"[{i}/{len(pdf_files)}] Loading: {filename}")
            
            try:
                docs = self.load_single_pdf(pdf_path)
                if docs:
                    self.all_documents.extend(docs)
                    self.loaded_files.append(pdf_path)
                    logger.info(f"  ✅ {len(docs)} page(s) extracted")
                else:
                    logger.warning(f"  ⚠️  No text extracted from {filename} — skipping")
                    self.failed_files.append(pdf_path)
            except Exception as e:
                logger.error(f"  ❌ Failed to load {filename}: {e}")
                self.failed_files.append(pdf_path)

        return self.all_documents

    def summary(self):
        """Print a summary of the PDF loading process"""
        logger.info("=" * 50)
        logger.info("PDF Loading Summary")
        logger.info("=" * 50)
        logger.info(f"  ✅ Loaded  : {len(self.loaded_files)}")
        logger.info(f"  ❌ Failed  : {len(self.failed_files)}")
        logger.info(f"  📄 Pages   : {len(self.all_documents)}")
        
        if self.failed_files:
            logger.warning("  Failed files:")
            for f in self.failed_files:
                logger.warning(f"    - {os.path.basename(f)}")
        
        logger.info("=" * 50)


class RecursiveCharacterTextSplitter:
    """
    Splits documents into chunks with overlapping windows
    Uses a hierarchy of separators to maintain context
    """
    
    def __init__(self, chunk_size: int = 400, chunk_overlap: int = 50, separators: Optional[List[str]] = None):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.separators = separators or ["\n\n", "\n", ". ", " ", ""]

    def split_text(self, text: str) -> List[str]:
        """Split text into chunks"""
        return self._split_text_recursive(text, self.separators)

    def _split_text_recursive(self, text: str, separators: List[str]) -> List[str]:
        final_chunks = []
        separator = separators[-1] if separators else ""
        current_separators = separators[:-1] if len(separators) > 1 else []

        splits = text.split(separator) if separator else list(text)
        current_chunk, current_length = [], 0

        for split in splits:
            split_to_use = split + separator if split != splits[-1] else split
            split_length = len(split_to_use)

            if split_length > self.chunk_size and current_separators:
                if current_chunk:
                    final_chunks.append("".join(current_chunk))
                    current_chunk, current_length = [], 0
                final_chunks.extend(self._split_text_recursive(split, current_separators))
            elif current_length + split_length <= self.chunk_size:
                current_chunk.append(split_to_use)
                current_length += split_length
            else:
                if current_chunk:
                    final_chunks.append("".join(current_chunk))
                if self.chunk_overlap > 0:
                    overlap_chars, overlap_chunk = 0, []
                    for s in reversed(current_chunk):
                        if overlap_chars + len(s) <= self.chunk_overlap:
                            overlap_chunk.insert(0, s)
                            overlap_chars += len(s)
                        else:
                            break
                    current_chunk = overlap_chunk
                    current_length = overlap_chars
                else:
                    current_chunk, current_length = [], 0
                current_chunk.append(split_to_use)
                current_length += split_length

        if current_chunk:
            final_chunks.append("".join(current_chunk))
        return final_chunks

    def split_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Split multiple documents into chunks"""
        split_docs = []
        file_chunk_counts: Dict[str, int] = {}

        for doc in documents:
            text = doc.get("page_content", "")
            metadata = doc.get("metadata", {}).copy()
            filename = metadata.get("filename", "unknown")
            chunks = self.split_text(text)

            for i, chunk in enumerate(chunks):
                if not chunk.strip():
                    continue
                chunk_metadata = metadata.copy()
                chunk_metadata.update({"chunk": i + 1, "total_chunks_in_page": len(chunks)})
                split_docs.append({"page_content": chunk, "metadata": chunk_metadata})
                file_chunk_counts[filename] = file_chunk_counts.get(filename, 0) + 1

        logger.info("=" * 50)
        logger.info("Text Splitting Summary")
        logger.info("=" * 50)
        logger.info(f"  📄 Input docs  : {len(documents)}")
        logger.info(f"  🧩 Total chunks: {len(split_docs)}")
        for fname, count in sorted(file_chunk_counts.items()):
            logger.info(f"    📎 {fname}: {count} chunks")
        logger.info("=" * 50)

        return split_docs

        return split_docs