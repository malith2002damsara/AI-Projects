# RAG ChatBot - Local Desktop Version

A Retrieval-Augmented Generation (RAG) chatbot that runs entirely on your local machine using Phi-2 LLM and PDF documents as knowledge base.

## 🚀 Features

- **100% Local Processing** - No cloud API calls (except optional Google Translate)
- **PDF-based Knowledge Base** - Load any PDF documents as your data source
- **Interactive Mode** - Chat with your documents in real-time
- **Sinhala Translation** - Optional translation support via Google Translate API
- **Vector Store Caching** - Fast loading after initial setup
- **Comprehensive Logging** - Track all operations with detailed logs
- **Error Handling** - Robust error handling throughout the application

## 📋 Requirements

### Models Required

Download and place these models in the ChatBot folder:

1. **Phi-2 LLM** (Microsoft)
   - Folder: `phi2/`
   - Download from: HuggingFace

2. **all-MiniLM-L6-v2** (Sentence Transformers)
   - Folder: `all-MiniLM-L6-v2/`
   - Download from: HuggingFace

### Python Dependencies

```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
ChatBot/
├── main.py                    # Main application entry point (CLI)
├── app.py                     # Flask web interface (NEW!)
├── config.py                  # Configuration and path management
├── logger.py                  # Logging configuration
├── requirements.txt           # Python dependencies
│
├── templates/                 # Flask HTML templates (NEW!)
│   └── index.html            # Web UI
│
├── data/
│   ├── pdfs/                 # Place your PDF files here
│   └── vector_store/         # Auto-generated vector database
│
├── models/
│   └── loader.py             # Model loading with error handling
│
├── pdf_loader/
│   └── loader.py             # PDF processing (PyPDF2 + pdfplumber)
│
├── rag/
│   ├── chain.py              # RAG chain orchestration
│   ├── prompt.py             # Prompt templates
│   ├── retriever.py          # Document retrieval
│   └── output_parser.py      # Response formatting
│
├── translation/
│   └── translator.py         # Google Translate integration
│
├── vectorstore/
│   └── store.py              # FAISS vector store management
│
└── logs/                      # Application logs (auto-generated)
```

## 🔧 Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Download Models

Download Phi-2 and all-MiniLM-L6-v2 models and place them in:
- `ChatBot/phi2/`
- `ChatBot/all-MiniLM-L6-v2/`

**Download Options:**

#### **Option A: From Google Drive** ⚡ **(Recommended - Faster!)**

**Direct Download Links:**

1. **Phi-2 Model (5.5GB)**:
   ```
   https://drive.google.com/drive/folders/1FYV7cXBjYf1lAKIGdiRQ7zmB_9iGvCc8?usp=sharing
   ```
   - Download folder: `phi2`
   - Place in: `ChatBot/phi2/`

2. **all-MiniLM-L6-v2 (90MB)**:
   ```
   https://drive.google.com/drive/folders/1OwrkNzx8wNssvq9kcIU9I8fH4-7_cH1C?usp=sharing
   ```
   - Download folder: `all-MiniLM-L6-v2`
   - Place in: `ChatBot/all-MiniLM-L6-v2/`

**Simple Steps:**
1. Click link → folder opens in browser
2. Right-click folder → "Download"
3. Extract ZIP to `ChatBot/` folder

See [`DRIVE_DOWNLOAD_GUIDE.md`](DRIVE_DOWNLOAD_GUIDE.md) for detailed download methods (browser, Python gdown, PowerShell).

#### **Option B: From HuggingFace** (Original Source)
- Phi-2: https://huggingface.co/microsoft/phi-2
- all-MiniLM-L6-v2: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

### 3. Add PDF Documents

Place your PDF files in:
```
ChatBot/data/pdfs/
```

You can organize them in subfolders if needed.

### 4. (Optional) Configure Google Translate

For Sinhala translation support, create a `.env` file:

```bash
GOOGLE_TRANSLATE_API_KEY=your_api_key_here
```

## 🎯 Usage

### Interactive Mode (Default)

```bash
python main.py
```

Commands in interactive mode:
- Type any question to get an answer
- Type `sinhala: <question>` for Sinhala translation
- Type `exit`, `quit`, or `q` to stop

Example:
```
💬 Your Question: What is machine learning?

[Answer will be displayed with sources]

💬 Your Question: sinhala: What is machine learning?

[Answer in Sinhala]

💬 Your Question: exit
👋 Exiting interactive mode. Goodbye!
```

### Web Interface (NEW! 🌐)

For a beautiful web-based interface:

```bash
python app.py
```

Then open your browser to:
```
http://localhost:5000
```

**Web Interface Features:**
- 🎨 Modern, responsive UI
- 📝 Easy question input with text area
- ☑️ One-click Sinhala translation toggle
- 📚 Source citations displayed beautifully
- 💻 Works on desktop and mobile
- 🌐 Can be accessed from other devices on your network

**Web Interface Screenshot:**
- Type your question in the text box
- Check "Translate to Sinhala" if needed
- Click "Ask Question" button
- See answer with source documents

### Example Mode

Run with pre-defined example queries:

```bash
python main.py --example
```

## 🛠️ Code Quality Improvements

### ✅ What Was Fixed

1. **Added Interactive Loop**
   - Real-time Q&A with your documents
   - Support for Sinhala translation requests
   - Graceful exit handling

2. **Comprehensive Logging**
   - Console and file logging
   - Different log levels (DEBUG, INFO, WARNING, ERROR)
   - Logs saved to `logs/chatbot.log`

3. **Error Handling**
   - Proper exception handling in all modules
   - Informative error messages
   - Graceful degradation (e.g., translation failures)

4. **Path Validation**
   - Check for model existence at startup
   - Auto-create data directories
   - Clear error messages for missing files

5. **Code Refactoring**
   - Simplified complex nested logic
   - Better function separation
   - Improved code readability

6. **Improved Exception Handling**
   - Specific exception types (FileNotFoundError, RuntimeError, etc.)
   - Detailed error logging
   - Fallback mechanisms

7. **Standardized Comments**
   - All comments in English
   - Clear documentation strings
   - Helpful inline comments

8. **Better Output Formatting**
   - Structured logging output
   - Clean console messages
   - Source citation for answers

## 📊 How It Works

1. **Initialization**
   - Validates configuration and model paths
   - Loads Phi-2 LLM and embedding model
   - Checks for existing vector store

2. **First Run (No Vector Store)**
   - Loads all PDFs from `data/pdfs/`
   - Splits documents into chunks (400 chars, 50 overlap)
   - Generates embeddings using all-MiniLM-L6-v2
   - Builds FAISS vector store
   - Saves for future use

3. **Subsequent Runs**
   - Loads cached vector store (fast startup)
   - Ready for queries immediately

4. **Query Processing**
   - User asks a question
   - Retrieves top-K relevant chunks (default: 4)
   - Constructs prompt with context
   - Generates answer using Phi-2
   - Parses and formats output
   - (Optional) Translates to Sinhala

## 🔍 Configuration

Edit `config.py` to customize:

```python
# Text splitting
CHUNK_SIZE = 400           # Characters per chunk
CHUNK_OVERLAP = 50         # Overlap between chunks

# Retrieval
RETRIEVER_K = 4            # Number of chunks to retrieve

# LLM Generation
MAX_NEW_TOKENS = 2048      # Max response length
TEMPERATURE = 0.7          # Creativity (0.0 - 1.0)
TOP_P = 0.9               # Nucleus sampling
```

## 📝 Logging

Logs are saved to `logs/chatbot.log` with detailed information:
- INFO: Normal operations
- WARNING: Non-critical issues
- ERROR: Failures and exceptions
- DEBUG: Detailed diagnostic information

View logs:
```bash
tail -f logs/chatbot.log
```

## 🐛 Troubleshooting

### Models not found
```
ERROR | Configuration validation failed:
  ❌ Phi-2 model not found at: C:\...\phi2
```
**Solution:** Download and place models in correct folders

### No PDFs found
```
ERROR | No PDFs found in: C:\...\data\pdfs
```
**Solution:** Add PDF files to `data/pdfs/` folder

### Translation fails
```
WARNING | GOOGLE_TRANSLATE_API_KEY not found in .env file
INFO | Translation skipped - returning original text
```
**Solution:** Add Google API key to `.env` file (or use without translation)

### GPU out of memory
**Solution:** The code automatically falls back to CPU if CUDA fails

## 🎨 Customization

### Change Prompt Template

Edit `rag/prompt.py`:
```python
RAG_TEMPLATE = """
Your custom prompt here...

Question: {question}
Context: {context}

Answer:"""
```

### Adjust Retrieval

Edit `main.py`:
```python
retriever = Retriever(
    vectorstore=vectorstore,
    search_type="similarity",
    search_kwargs={"k": 8}  # Retrieve 8 chunks instead of 4
)
```

## 📚 Technical Stack

- **LLM:** Microsoft Phi-2 (2.7B parameters)
- **Embeddings:** all-MiniLM-L6-v2 (Sentence Transformers)
- **Vector Store:** FAISS (Facebook AI Similarity Search)
- **PDF Processing:** PyPDF2 + pdfplumber (fallback)
- **Framework:** Pure Python (no LangChain dependency)

## 🤝 Contributing

Improvements made:
- ✅ Interactive query loop
- ✅ Comprehensive logging system
- ✅ Robust error handling
- ✅ Path validation
- ✅ Code refactoring
- ✅ Documentation

## 📄 License

This project is for educational and research purposes.

## 🙏 Acknowledgments

- Microsoft for Phi-2 model
- Sentence Transformers for embeddings
- FAISS for vector search
- PyPDF2 and pdfplumber for PDF processing

---

**Need help?** Check the logs in `logs/chatbot.log` for detailed error information.
