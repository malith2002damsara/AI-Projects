"""
Flask Web Interface for RAG ChatBot
=====================================
Run: python app.py
Access: http://localhost:5000

A web-based interface for asking questions and getting answers from your PDF documents.
"""

import os
import sys
import threading
import webbrowser
from flask import Flask, render_template, request, jsonify, session
from werkzeug.security import generate_password_hash
import secrets

# Add project root to path
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
from rag.output_parser import TextOutputParser, extract_answer
from translation.translator import translate_response
from logger import setup_logger

# Setup Flask app
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
logger = setup_logger(__name__)

# Global variables for model components
pipe = None
embedding_model = None
chain_func = None


def initialize_system():
    """Initialize all models and components"""
    global pipe, embedding_model, chain_func
    
    logger.info("=" * 60)
    logger.info("🌐 Starting Flask Web Interface for RAG ChatBot")
    logger.info("=" * 60)
    
    # Validate configuration
    try:
        validation = validate_paths(strict=False)
        if not validation["valid"]:
            logger.error("Configuration validation failed:")
            for error in validation["errors"]:
                logger.error(f"  ❌ {error}")
            return False
        
        for warning in validation["warnings"]:
            logger.warning(f"  ⚠️  {warning}")
    except Exception as e:
        logger.error(f"Configuration error: {e}")
        return False
    
    # Load models
    try:
        logger.info("Loading models...")
        pipe = load_llm_pipeline()
        embedding_model = load_embedding_model()
    except Exception as e:
        logger.error(f"Failed to load models: {e}")
        return False
    
    # Load or build vector store
    try:
        vectorstore = VectorStore(embedding_model, index_path=VECTOR_STORE_PATH)
        
        if not vectorstore.documents:
            logger.info("Vector store not found. Building from PDFs...")
            os.makedirs(PDF_FOLDER, exist_ok=True)
            
            directory_loader = RAGPDFDirectoryLoader(PDF_FOLDER)
            all_docs = directory_loader.load_all()
            directory_loader.summary()
            
            if not all_docs:
                logger.error(f"No PDFs found in: {PDF_FOLDER}")
                return False
            
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP
            )
            splits = text_splitter.split_documents(all_docs)
            
            vectorstore.add_documents(splits)
            vectorstore.save(VECTOR_STORE_PATH)
            logger.info(f"✅ Vector store built and saved")
        else:
            logger.info(f"✅ Vector store loaded: {len(vectorstore.documents)} chunks")
    except Exception as e:
        logger.error(f"Failed to setup vector store: {e}")
        return False
    
    # Build RAG chain
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
        logger.info("=" * 60)
        return True
    except Exception as e:
        logger.error(f"Failed to build RAG chain: {e}")
        return False


# Initialize system on startup
logger.info("Initializing ChatBot system...")
if not initialize_system():
    logger.error("❌ System initialization failed. Please check logs.")
    sys.exit(1)


@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')


@app.route('/api/ask', methods=['POST'])
def ask_question():
    """Handle question and return answer"""
    try:
        data = request.get_json()
        question = data.get('question', '').strip()
        translate_sinhala = data.get('translate', False)
        
        if not question:
            return jsonify({
                'success': False,
                'error': 'Please provide a question'
            }), 400
        
        logger.info(f"💬 Web query: {question[:100]}...")
        
        # Run query through chain
        response = chain_func(question)
        
        # Translate if requested
        if translate_sinhala:
            logger.info("Translating to Sinhala...")
            response = translate_response(response, extract_answer)
        
        # Extract answer and sources
        answer = extract_answer(response)
        sources = response.get('source_documents', [])
        
        # Format sources
        formatted_sources = []
        seen_sources = set()
        
        for source in sources:
            filename = source.get('filename', 'Unknown')
            page = source.get('page', 'N/A')
            source_key = f"{filename}_{page}"
            
            if source_key not in seen_sources:
                formatted_sources.append({
                    'filename': filename,
                    'page': page
                })
                seen_sources.add(source_key)
        
        logger.info("✅ Query completed successfully")
        
        return jsonify({
            'success': True,
            'answer': answer,
            'sources': formatted_sources,
            'question': question
        })
        
    except Exception as e:
        logger.error(f"Error processing query: {e}")
        return jsonify({
            'success': False,
            'error': f'Error processing your question: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'models_loaded': pipe is not None and embedding_model is not None,
        'chain_ready': chain_func is not None
    })


@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors"""
    return jsonify({'success': False, 'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors"""
    logger.error(f"Internal server error: {e}")
    return jsonify({'success': False, 'error': 'Internal server error'}), 500


if __name__ == '__main__':
    logger.info("\n" + "=" * 60)
    logger.info("🌐 Flask server starting...")
    logger.info("📍 Access at: http://localhost:5000")
    logger.info("🛑 Press Ctrl+C to stop")
    logger.info("=" * 60 + "\n")

    # Auto-open browser after Flask starts
    def open_browser():
        webbrowser.open("http://127.0.0.1:5000")
    threading.Timer(1.5, open_browser).start()

    # Run Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
