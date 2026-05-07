import os
import sys
from pathlib import Path

# ═══════════════════════════════════════════════════════════════
# Model Paths
# ═══════════════════════════════════════════════════════════════
# Models should be in separate folders within the ChatBot directory
BASE_DIR = Path(__file__).parent
PHI2_MODEL_PATH = BASE_DIR / "phi2"
EMBEDDING_MODEL_PATH = BASE_DIR / "all-MiniLM-L6-v2"

# ═══════════════════════════════════════════════════════════════
# Data Paths
# ═══════════════════════════════════════════════════════════════
PDF_FOLDER = BASE_DIR / "data" / "pdfs"
VECTOR_STORE_PATH = BASE_DIR / "data" / "vector_store" / "index"

# ═══════════════════════════════════════════════════════════════
# Text Splitting Configuration
# ═══════════════════════════════════════════════════════════════
CHUNK_SIZE = 400
CHUNK_OVERLAP = 50

# ═══════════════════════════════════════════════════════════════
# Retriever Configuration
# ═══════════════════════════════════════════════════════════════
RETRIEVER_K = 2  # Number of top documents to retrieve

# ═══════════════════════════════════════════════════════════════
# LLM Generation Parameters
# ═══════════════════════════════════════════════════════════════
MAX_NEW_TOKENS = 300
TEMPERATURE = 0.7
TOP_P = 0.9


# ═══════════════════════════════════════════════════════════════
# Path Validation
# ═══════════════════════════════════════════════════════════════
def validate_paths(strict: bool = False) -> dict:
    """
    Validate that required paths exist
    
    Args:
        strict: If True, raises FileNotFoundError for missing paths
               If False, only returns warnings
    
    Returns:
        Dictionary with validation results
    """
    validation_results = {
        "valid": True,
        "warnings": [],
        "errors": []
    }
    
    # Convert to Path objects if they are strings (for compatibility)
    phi2_path = Path(PHI2_MODEL_PATH) if isinstance(PHI2_MODEL_PATH, str) else PHI2_MODEL_PATH
    embedding_path = Path(EMBEDDING_MODEL_PATH) if isinstance(EMBEDDING_MODEL_PATH, str) else EMBEDDING_MODEL_PATH
    pdf_folder = Path(PDF_FOLDER) if isinstance(PDF_FOLDER, str) else PDF_FOLDER
    vector_store_path = Path(VECTOR_STORE_PATH) if isinstance(VECTOR_STORE_PATH, str) else VECTOR_STORE_PATH
    
    # Check model paths
    if not phi2_path.exists():
        msg = f"Phi-2 model not found at: {phi2_path}"
        validation_results["errors"].append(msg)
        validation_results["valid"] = False
        if strict:
            raise FileNotFoundError(msg)
    
    if not embedding_path.exists():
        msg = f"Embedding model not found at: {embedding_path}"
        validation_results["errors"].append(msg)
        validation_results["valid"] = False
        if strict:
            raise FileNotFoundError(msg)
    
    # Check/create data directories
    if not pdf_folder.exists():
        validation_results["warnings"].append(
            f"PDF folder will be created: {pdf_folder}"
        )
        pdf_folder.mkdir(parents=True, exist_ok=True)
    
    vector_store_dir = vector_store_path.parent
    if not vector_store_dir.exists():
        validation_results["warnings"].append(
            f"Vector store directory will be created: {vector_store_dir}"
        )
        vector_store_dir.mkdir(parents=True, exist_ok=True)
    
    return validation_results


# Convert Path objects to strings for backward compatibility
PHI2_MODEL_PATH = str(PHI2_MODEL_PATH)
EMBEDDING_MODEL_PATH = str(EMBEDDING_MODEL_PATH)
PDF_FOLDER = str(PDF_FOLDER)
VECTOR_STORE_PATH = str(VECTOR_STORE_PATH)