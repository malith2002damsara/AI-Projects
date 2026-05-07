import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, AutoConfig, pipeline
from sentence_transformers import SentenceTransformer
from config import PHI2_MODEL_PATH, EMBEDDING_MODEL_PATH, MAX_NEW_TOKENS, TEMPERATURE, TOP_P
from logger import setup_logger

logger = setup_logger(__name__)
device = "cuda" if torch.cuda.is_available() else "cpu"


def load_llm_pipeline():
    """
    Load the Phi-2 language model pipeline with proper error handling
    
    Returns:
        Pipeline object for text generation
        
    Raises:
        FileNotFoundError: If model files are not found
        RuntimeError: If model loading fails
    """
    try:
        logger.info(f"Using device: {device}")
        
        # Validate model path exists
        if not os.path.exists(PHI2_MODEL_PATH):
            raise FileNotFoundError(
                f"Phi-2 model not found at: {PHI2_MODEL_PATH}\n"
                f"Please download the model and place it in the correct folder."
            )

        logger.info("Loading tokenizer...")
        tokenizer = AutoTokenizer.from_pretrained(
            PHI2_MODEL_PATH,
            local_files_only=True,
            trust_remote_code=True
        )

        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
            tokenizer.pad_token_id = tokenizer.eos_token_id
            logger.debug("Set pad_token to eos_token")

        logger.info("Loading model config...")
        config = AutoConfig.from_pretrained(
            PHI2_MODEL_PATH,
            local_files_only=True,
            trust_remote_code=True
        )
        config.pad_token_id = tokenizer.eos_token_id

        logger.info("Loading Phi-2 model (this may take a few moments)...")
        model = AutoModelForCausalLM.from_pretrained(
            PHI2_MODEL_PATH,
            config=config,
            local_files_only=True,
            trust_remote_code=True,
            torch_dtype=torch.float16 if device == "cuda" else torch.float32,
            device_map="auto"
        )
        model.eval()

        pipe = pipeline(
            task="text-generation",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=MAX_NEW_TOKENS,
            temperature=TEMPERATURE,
            top_p=TOP_P,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )

        logger.info("✅ Phi-2 model loaded successfully!")
        return pipe
        
    except FileNotFoundError as e:
        logger.error(f"Model file not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Failed to load LLM pipeline: {e}")
        raise RuntimeError(f"Could not load Phi-2 model: {e}")


def load_embedding_model():
    """
    Load the sentence embedding model with proper error handling
    
    Returns:
        SentenceTransformer model for embeddings
        
    Raises:
        FileNotFoundError: If embedding model files are not found
        RuntimeError: If model loading fails
    """
    try:
        # Validate model path exists
        if not os.path.exists(EMBEDDING_MODEL_PATH):
            raise FileNotFoundError(
                f"Embedding model not found at: {EMBEDDING_MODEL_PATH}\n"
                f"Please download all-MiniLM-L6-v2 and place it in the correct folder."
            )
        
        logger.info("Loading embedding model...")
        embedding_model = SentenceTransformer(EMBEDDING_MODEL_PATH, device=device)
        logger.info("✅ Embedding model loaded successfully!")
        return embedding_model
        
    except FileNotFoundError as e:
        logger.error(f"Embedding model file not found: {e}")
        raise
    except Exception as e:
        logger.error(f"Failed to load embedding model: {e}")
        raise RuntimeError(f"Could not load embedding model: {e}")