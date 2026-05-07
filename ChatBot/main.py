"""
RAG ChatBot - Local Desktop Version
=====================================
Usage: python main.py

Setup Instructions:
1. Place PDF files in: data/pdfs/ folder
2. Ensure models are in separate folders within ChatBot directory:
   - phi2/                   (LLM model)
   - all-MiniLM-L6-v2/       (Embedding model)
3. (Optional) Add GOOGLE_TRANSLATE_API_KEY to .env for Sinhala translation

The first run will load PDFs and build a vector store (saved for reuse).
"""

import os
import sys

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from dotenv import load_dotenv
load_dotenv()

from config import (
    PDF_FOLDER, VECTOR_STORE_PATH, CHUNK_SIZE, CHUNK_OVERLAP, RETRIEVER_K,
    validate_paths
)
from models.loader import load_llm_pipeline, load_embedding_model
from pdf_loader.loader import RAGPDFDirectoryLoader, RecursiveCharacterTextSplitter
from vectorstore.store import VectorStore
from rag.retriever import Retriever
from rag.prompt import get_prompt_template
from rag.chain import create_chain
from rag.output_parser import TextOutputParser, print_answer, extract_answer
from translation.translator import translate_response
from logger import setup_logger

logger = setup_logger(__name__)


# ═══════════════════════════════════════════════
# STEP 0: Validate Configuration
# ═══════════════════════════════════════════════
logger.info("=" * 60)
logger.info("🚀 Starting RAG ChatBot (Local Mode)")
logger.info("=" * 60)

try:
    validation = validate_paths(strict=False)
    if not validation["valid"]:
        logger.error("Configuration validation failed:")
        for error in validation["errors"]:
            logger.error(f"  ❌ {error}")
        logger.info("\nPlease download required models and try again.")
        sys.exit(1)
    
    for warning in validation["warnings"]:
        logger.warning(f"  ⚠️  {warning}")
        
except Exception as e:
    logger.error(f"Configuration error: {e}")
    sys.exit(1)


# ═══════════════════════════════════════════════
# STEP 1: Load Models
# ═══════════════════════════════════════════════
try:
    pipe = load_llm_pipeline()
    embedding_model = load_embedding_model()
except Exception as e:
    logger.error(f"Failed to load models: {e}")
    sys.exit(1)


# ═══════════════════════════════════════════════
# STEP 2: Load or Build Vector Store
# ═══════════════════════════════════════════════
vectorstore = VectorStore(embedding_model, index_path=VECTOR_STORE_PATH)

# If vector store is empty, load PDFs and build it
if not vectorstore.documents:
    logger.info("Vector store not found. Building from PDFs...")

    # Ensure PDF folder exists
    os.makedirs(PDF_FOLDER, exist_ok=True)

    # Load PDFs
    try:
        directory_loader = RAGPDFDirectoryLoader(PDF_FOLDER)
        all_docs = directory_loader.load_all()
        directory_loader.summary()

        if not all_docs:
            logger.error(f"No PDFs found in: {PDF_FOLDER}")
            logger.info("Please add PDF files to the folder and re-run.")
            sys.exit(1)

        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        splits = text_splitter.split_documents(all_docs)

        # Add to vector store and save
        vectorstore.add_documents(splits)
        vectorstore.save(VECTOR_STORE_PATH)
        logger.info(f"✅ Vector store built and saved: {VECTOR_STORE_PATH}")
        
    except Exception as e:
        logger.error(f"Failed to build vector store: {e}")
        sys.exit(1)
else:
    logger.info(f"✅ Vector store loaded: {len(vectorstore.documents)} chunks ready.")


# ═══════════════════════════════════════════════
# STEP 3: Build RAG Chain
# ═══════════════════════════════════════════════
try:
    retriever = Retriever(
        vectorstore=vectorstore,
        search_type="similarity",
        search_kwargs={"k": RETRIEVER_K}
    )

    prompt = get_prompt_template()
    output_parser = TextOutputParser()
    chain_func = create_chain(retriever, prompt, pipe, output_parser)

    logger.info("✅ RAG chain ready!")
    
except Exception as e:
    logger.error(f"Failed to build RAG chain: {e}")
    sys.exit(1)


# ═══════════════════════════════════════════════
# STEP 4: Query Functions
# ═══════════════════════════════════════════════
def run_query(question: str, sinhala: bool = False):
    """
    Execute a query through the RAG chain
    
    Args:
        question: The question to ask
        sinhala: Whether to translate the answer to Sinhala
    
    Returns:
        Response dictionary with answer and sources
    """
    logger.info(f"Running query: {question[:100]}...")
    
    try:
        response = chain_func(question)

        if sinhala:
            logger.info("Translating response to Sinhala...")
            response = translate_response(response, extract_answer)

        print_answer(response)
        return response
        
    except Exception as e:
        logger.error(f"Query execution failed: {e}")
        return {"answer": f"Error: {str(e)}", "question": question}


# ═══════════════════════════════════════════════
# STEP 5: Interactive Mode
# ═══════════════════════════════════════════════
def interactive_mode():
    """Run the chatbot in interactive mode"""
    logger.info("\n" + "=" * 60)
    logger.info("🤖 Entering Interactive Mode")
    logger.info("=" * 60)
    print("\nCommands:")
    print("  - Type your question to get an answer")
    print("  - Type 'sinhala: <question>' for Sinhala translation")
    print("  - Type 'exit' or 'quit' to stop")
    print("=" * 60 + "\n")
    
    while True:
        try:
            user_input = input("\n💬 Your Question: ").strip()
            
            if not user_input:
                continue
            
            # Check for exit command
            if user_input.lower() in ['exit', 'quit', 'q', 'bye']:
                logger.info("👋 Exiting interactive mode. Goodbye!")
                break
            
            # Check for Sinhala translation request
            if user_input.lower().startswith('sinhala:'):
                question = user_input[8:].strip()
                if question:
                    run_query(question, sinhala=True)
                else:
                    print("⚠️  Please provide a question after 'sinhala:'")
            else:
                run_query(user_input, sinhala=False)
                
        except KeyboardInterrupt:
            logger.info("\n\n👋 Interrupted by user. Exiting...")
            break
        except Exception as e:
            logger.error(f"Error in interactive mode: {e}")
            print(f"❌ An error occurred: {e}")


# ═══════════════════════════════════════════════
# Main Entry Point
# ═══════════════════════════════════════════════
if __name__ == "__main__":
    # Check if running in example mode or interactive mode
    if len(sys.argv) > 1 and sys.argv[1] == "--example":
        # Run example queries
        logger.info("Running in example mode...")
        
        # English answer
        run_query(
            "Provide a research background and conceptual framework relevant to the research question: "
            "What are the reasons why university students use cosmetics?"
        )

        # Sinhala answer
        run_query(
            "Provide a research background and conceptual framework relevant to the research question: "
            "What are the reasons why university students use cosmetics? Also give statistical data if available.",
            sinhala=True
        )
    else:
        # Run interactive mode by default
        interactive_mode()