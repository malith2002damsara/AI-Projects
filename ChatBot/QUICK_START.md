# 🚀 Quick Start Guide

## Method 1: Command Line (Terminal)

### Basic Usage
```bash
# Start interactive mode
python main.py

# Type your questions
💬 Your Question: What is in the documents?
```

### Sinhala Translation
```bash
# In interactive mode, type:
sinhala: Your question here
```

### Exit
```bash
# Type any of these:
exit
quit
q
```

---

## Method 2: Web Interface (Recommended! 🌐)

### Start Web Server
```bash
python app.py
```

### Open Browser
```
http://localhost:5000
```

### Use Web Interface
1. ✍️ Type question in text box
2. ☑️ Check "Translate to Sinhala" (optional)
3. 🚀 Click "Ask Question"
4. 📖 Read answer with sources!

---

## First Time Setup

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Download Models
Download these and place in ChatBot folder:
- `phi2/` - Phi-2 LLM model
- `all-MiniLM-L6-v2/` - Embedding model

### 3. Add PDFs
```
ChatBot/
└── data/
    └── pdfs/
        ├── your-document-1.pdf
        ├── your-document-2.pdf
        └── ...
```

### 4. Run!
```bash
# Web interface (easier)
python app.py

# OR command line
python main.py
```

---

## Access from Phone/Tablet

### Find Your Computer's IP
**Windows:**
```powershell
ipconfig
# Look for IPv4 Address (e.g., 192.168.1.100)
```

**Linux/Mac:**
```bash
ifconfig
# Look for inet address
```

### Open on Mobile
```
http://YOUR_IP_ADDRESS:5000
# Example: http://192.168.1.100:5000
```

**Note:** Make sure phone and computer are on same WiFi network!

---

## Troubleshooting

### Port Already in Use
If port 5000 is busy, edit `app.py`:
```python
# Change last line to:
app.run(debug=True, host='0.0.0.0', port=5001)
```

Then access: `http://localhost:5001`

### Models Not Found
```
ERROR | Phi-2 model not found
```
**Fix:** Download models and place in correct folders

### No PDFs Found
```
ERROR | No PDFs found in: data\pdfs
```
**Fix:** Add PDF files to `data/pdfs/` folder

### Slow Performance
- First run is slow (building vector store)
- Subsequent runs are faster
- GPU makes it much faster (but CPU works too)

---

## Tips

### 💡 Best Practices
1. Use Web Interface for better experience
2. Add quality PDFs (scanned images don't work well)
3. First question takes longer (models loading)
4. Check `logs/chatbot.log` for debugging

### 🎯 Good Questions
- "What is the main topic of the documents?"
- "Summarize the key findings"
- "What does the research say about X?"
- "List the main conclusions"

### 🚫 Avoid
- Very short questions (be specific)
- Questions unrelated to your PDFs
- Asking about images/charts (text only)

---

## File Structure Check

Before running, verify:
```
ChatBot/
├── app.py ✅
├── main.py ✅
├── templates/
│   └── index.html ✅
├── phi2/ ✅ (model files)
├── all-MiniLM-L6-v2/ ✅ (model files)
└── data/
    └── pdfs/ ✅ (your PDFs here)
```

---

## Command Reference

### Command Line
```bash
# Interactive mode (default)
python main.py

# Example mode (test)
python main.py --example

# Exit interactive mode
Type: exit, quit, or q
```

### Web Interface
```bash
# Start server
python app.py

# Stop server
Press Ctrl+C in terminal
```

### Managing PDFs
```bash
# Add new PDFs
# 1. Add files to data/pdfs/
# 2. Delete vector store:
Remove-Item -Recurse -Force data\vector_store\
# 3. Re-run (rebuilds automatically):
python app.py
```

---

## Quick Commands (Windows PowerShell)

```powershell
# Install everything
pip install -r requirements.txt

# Start web interface
python app.py

# Check if server is running
curl http://localhost:5000/api/health

# View logs in real-time
Get-Content logs\chatbot.log -Wait

# Rebuild vector store
Remove-Item -Recurse -Force data\vector_store\
python app.py
```

---

## Need Help?

1. 📋 Check `logs/chatbot.log` for errors
2. 📖 Read `HOW_TO_RUN.md` for detailed guide
3. 📚 Read `README.md` for full documentation
4. 🔍 Verify all models and PDFs are in place

---

**Enjoy using RAG ChatBot! 🎉**

සතුටින් භාවිතා කරන්න! 🇱🇰
