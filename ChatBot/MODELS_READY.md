# 🎯 Models Download කරන්න - Quick Instructions

## 📥 **Easy Steps to Get Your ChatBot Running:**

### **Step 1: Download Models** (5-10 minutes)

#### **Model 1: Phi-2** (5.5GB) - Main Brain 🧠
1. Open link: https://drive.google.com/drive/folders/1FYV7cXBjYf1lAKIGdiRQ7zmB_9iGvCc8?usp=sharing
2. Click **⋮** (three dots) → **"Download"**
3. Wait for ZIP download (5.5GB - takes time!)
4. Extract the **`phi2`** folder
5. Copy `phi2/` to: `C:\Users\damsara\Desktop\ChatBot\phi2\`

#### **Model 2: all-MiniLM-L6-v2** (90MB) - Fast Search 🔍
1. Open link: https://drive.google.com/drive/folders/1OwrkNzx8wNssvq9kcIU9I8fH4-7_cH1C?usp=sharing
2. Click **⋮** (three dots) → **"Download"**
3. Wait for ZIP download (90MB - fast!)
4. Extract the **`all-MiniLM-L6-v2`** folder
5. Copy `all-MiniLM-L6-v2/` to: `C:\Users\damsara\Desktop\ChatBot\all-MiniLM-L6-v2\`

---

### **Step 2: Verify Folder Structure** ✅

After copying, your folder should look like this:
```
C:\Users\damsara\Desktop\ChatBot\
├── phi2/
│   ├── config.json
│   ├── model.safetensors (or .bin files)
│   ├── tokenizer.json
│   └── ... (other files)
│
├── all-MiniLM-L6-v2/
│   ├── config.json
│   ├── pytorch_model.bin
│   ├── tokenizer.json
│   └── ... (other files)
│
├── data/
│   └── pdfs/         ← Put your PDF files here!
│
├── app.py
├── main.py
└── ... (other project files)
```

**⚠️ Common Mistake:** After extracting, sometimes you get `phi2/phi2/` (nested folder). If this happens:
- Move the **inner** `phi2/` folder to the ChatBot directory
- Delete the empty outer folder

---

### **Step 3: Add PDF Documents** 📚

1. Place your PDF files in: `C:\Users\damsara\Desktop\ChatBot\data\pdfs\`
2. You can add as many PDFs as you want
3. Organize in subfolders if needed (e.g., `pdfs/biology/`, `pdfs/history/`)

---

### **Step 4: Run the ChatBot** 🚀

#### **Option A: Web Interface** (Recommended)
```powershell
cd C:\Users\damsara\Desktop\ChatBot
python app.py
```
Then open browser: **http://localhost:5000**

#### **Option B: Command Line**
```powershell
cd C:\Users\damsara\Desktop\ChatBot
python main.py
```

---

## 🎉 **That's It!**

First run will take 2-3 minutes to:
- Load models (Phi-2 is big!)
- Process PDFs
- Build vector store

After that, it's instant! ⚡

---

## ❓ Troubleshooting

**Models not found error?**
- Double-check folder names: `phi2` and `all-MiniLM-L6-v2` (exact spelling!)
- Make sure they're in the ChatBot folder (not in subfolders)

**Out of memory?**
- Close other programs
- You need at least 8GB RAM for Phi-2

**PDF errors?**
- Make sure PDFs have selectable text (not just scanned images)
- Try with 1-2 PDFs first to test

**Need help?**
- Check `logs/chatbot.log` for detailed error messages
- See `HOW_TO_RUN.md` for full documentation

---

## 📋 Quick Checklist

- [ ] Downloaded `phi2` from Drive (5.5GB)
- [ ] Downloaded `all-MiniLM-L6-v2` from Drive (90MB)
- [ ] Extracted both ZIP files
- [ ] Copied folders to ChatBot directory
- [ ] Verified folder structure (no nested folders!)
- [ ] Added PDF files to `data/pdfs/`
- [ ] Ran `python app.py`
- [ ] Opened http://localhost:5000 in browser
- [ ] 🎉 Chatbot working!

---

**Drive Links Again (for easy access):**
- Phi-2: https://drive.google.com/drive/folders/1FYV7cXBjYf1lAKIGdiRQ7zmB_9iGvCc8?usp=sharing
- all-MiniLM-L6-v2: https://drive.google.com/drive/folders/1OwrkNzx8wNssvq9kcIU9I8fH4-7_cH1C?usp=sharing
