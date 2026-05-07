# අරඹන්න කලින් කියවන්න (HOW TO RUN - Sinhala/English)

## 🇱🇰 සිංහලෙන් (Sinhala Instructions)

### පළමුව Setup කරන්න

#### 1. Python Install කරන්න
- Python 3.8 හෝ ඊට වැඩි version එකක් ඕනේ
- Download: https://www.python.org/downloads/

#### 2. Dependencies Install කරන්න
```bash
pip install -r requirements.txt
```

#### 3. Models Download කරන්න

**අනිවාර්යයෙන්ම මේ models දෙක download කරන්න:**

##### a) Phi-2 Model (LLM)
- HuggingFace: https://huggingface.co/microsoft/phi-2
- Download කරලා `ChatBot/phi2/` folder එකේ තියන්න

##### b) all-MiniLM-L6-v2 (Embeddings)
- HuggingFace: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
- Download කරලා `ChatBot/all-MiniLM-L6-v2/` folder එකේ තියන්න

**Folder structure මෙහෙම තියෙන්න ඕනේ:**
```
ChatBot/
├── phi2/
│   ├── config.json
│   ├── pytorch_model.bin
│   └── ... (other model files)
│
├── all-MiniLM-L6-v2/
│   ├── config.json
│   ├── pytorch_model.bin
│   └── ... (other model files)
│
└── ... (other project files)
```

#### 4. PDF Files එකතු කරන්න
- ඔබේ PDF files `ChatBot/data/pdfs/` folder එකට copy කරන්න
- කීයක් තිබුණත් කමක් නැහැ
- Subfolders වලත් දාන්න පුළුවන්

#### 5. (Optional) Google Translate සඳහා
සිංහල translation ඕනේ නම් `.env` file එකක් හදන්න:
```
GOOGLE_TRANSLATE_API_KEY=your_api_key_here
```

---

### 🚀 Run කරන්න

#### Option 1: Command Line (Terminal)

##### Interactive Mode
```bash
python main.py
```
- Questions type කරන්න
- `exit` type කරන්න නවත්වන්න

##### Example Mode (Test කරන්න)
```bash
python main.py --example
```

#### Option 2: Flask Web Interface 🌐

##### Web UI එක Start කරන්න
```bash
python app.py
```

##### Browser එකෙන් Open කරන්න
```
http://localhost:5000
```

දැන් web page එකේ:
- Question box එකට type කරන්න
- "Ask Question" click කරන්න
- Answer එක පෙන්වයි sources සමඟ
- "Translate to Sinhala" checkbox එක tick කරන්න සිංහල translation එකට

---

### ⚠️ Common Problems & Solutions

#### Problem 1: "Models not found"
```
ERROR | Phi-2 model not found at: C:\...\phi2
```
**විසඳුම:** Models download කරලා නිවැරදි folders වල තියන්න

#### Problem 2: "No PDFs found"
```
ERROR | No PDFs found in: C:\...\data\pdfs
```
**විසඳුම:** PDF files `data/pdfs/` folder එකට දාන්න

#### Problem 3: "CUDA out of memory"
**විසඳුම:** GPU නැත්නම් automatic එක්ම CPU use කරයි (slow වෙන්න පුළුවන්)

#### Problem 4: Port already in use (Flask)
```
Address already in use
```
**විසඳුම:** `app.py` file එකේ port number එක වෙනස් කරන්න:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # 5000 වෙනුවට 5001
```

---

### 📊 First Run (පළමු වතාවට run කරනකොට)

පළමු වතාවට run කරනකොට:
1. Models load වෙනවා (මිනිත්තු 2-3ක් ගත වෙනවා)
2. PDFs load වෙනවා
3. Vector store build වෙනවා (PDFs ගණන අනුව කාලය වෙනස්)
4. Save වෙනවා future use එකට

දෙවෙනි වතාවේ සිට:
- පරන vector store load වෙනවා (ඉක්මනින්)
- Models load වෙනවා
- Ready!

---

## 🇬🇧 English Instructions

### Quick Start

#### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 2. Download Models
- Phi-2: Place in `ChatBot/phi2/`
- all-MiniLM-L6-v2: Place in `ChatBot/all-MiniLM-L6-v2/`

#### 3. Add PDF Files
- Place PDFs in `ChatBot/data/pdfs/`

#### 4. Run

**Command Line:**
```bash
python main.py
```

**Web Interface:**
```bash
python app.py
```
Then open: http://localhost:5000

---

### 🔧 System Requirements

**Minimum:**
- Python 3.8+
- 8GB RAM
- 10GB disk space

**Recommended:**
- Python 3.10+
- 16GB RAM
- NVIDIA GPU with 6GB+ VRAM (optional, for faster processing)
- 20GB disk space

---

### 📝 Usage Examples

#### Command Line Mode:
```
💬 Your Question: What is machine learning?
[Answer with sources will be displayed]

💬 Your Question: sinhala: What is machine learning?
[Answer in Sinhala will be displayed]

💬 Your Question: exit
👋 Goodbye!
```

#### Web Interface:
1. Type your question in the text box
2. (Optional) Check "Translate to Sinhala"
3. Click "Ask Question"
4. See answer with source documents

---

### 📂 File Structure Check

Run කරන්න කලින් මේ structure එක තියෙනවද check කරන්න:

```
ChatBot/
├── app.py                 ← Flask web app (NEW!)
├── main.py                ← CLI app
├── config.py
├── logger.py
├── requirements.txt
├── .env (optional)
│
├── phi2/                  ← Model files
├── all-MiniLM-L6-v2/      ← Embedding model
│
├── data/
│   ├── pdfs/              ← Your PDF files HERE
│   └── vector_store/      ← Auto-generated
│
├── models/
├── pdf_loader/
├── rag/
├── translation/
├── vectorstore/
└── logs/                  ← Auto-generated
```

---

### 🎯 Pro Tips

1. **First Run:** අනිවාර්යයෙන්ම internet connection අවශ්‍ය නැහැ (models download කර තියෙනවා නම්)
2. **PDF Quality:** හොඳ quality PDFs use කරන්න (scanned images වැඩ කරන්නේ නැහැ)
3. **GPU:** CUDA GPU තියෙනවා නම් automatic එකම use කරයි
4. **Logs:** Problems තියෙනවා නම් `logs/chatbot.log` බලන්න
5. **Vector Store:** PDFs වෙනස් කළාම `data/vector_store/` delete කරලා rebuild කරන්න

---

### 🔄 Rebuilding Vector Store

PDFs වෙනස් කරපු නම්:
```bash
# Delete vector store
rm -rf data/vector_store/

# Re-run (will rebuild automatically)
python main.py
```

Windows එකේ:
```powershell
Remove-Item -Recurse -Force data\vector_store\
python main.py
```

---

### 🌐 Access from Other Devices

Flask app එක network එකේ තියෙන අනික් devices වලින් access කරන්න:

1. `app.py` එකේ `host='0.0.0.0'` තියෙනවද check කරන්න
2. Your computer's IP address එක හොයාගන්න:
   ```bash
   ipconfig  # Windows
   ifconfig  # Linux/Mac
   ```
3. අනික් device එකේ browser එකෙන්:
   ```
   http://YOUR_IP_ADDRESS:5000
   ```

---

### 👨‍💻 Developer Mode

Debug information ඕනේ නම්:
```bash
# Set debug logging
python main.py
```

Logs real-time එකේ බලන්න:
```bash
tail -f logs/chatbot.log  # Linux/Mac
Get-Content logs\chatbot.log -Wait  # PowerShell
```

---

### ❓ Help

Problems තියෙනවා නම්:
1. `logs/chatbot.log` file එක check කරන්න
2. Models හරියටම download වෙලා තියෙනවද verify කරන්න
3. PDF files readable කියලා check කරන්න
4. Python version check කරන්න: `python --version`

---

**සතුටින් භාවිතා කරන්න! 🎉**

Got questions? Check the logs or documentation!
