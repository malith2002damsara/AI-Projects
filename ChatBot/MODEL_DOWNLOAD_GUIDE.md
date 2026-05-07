# 📥 Models කොහෙන් Download කරන්නේ? (Model Download Guide)

## 🎯 Models 2ක් ඕනේ:

### 1. **Phi-2** (LLM Model)
### 2. **all-MiniLM-L6-v2** (Embedding Model)

---

## 📍 තියෙන්න ඕනේ කොහෙද? (Where to Place)

Models **ChatBot folder එකේම** තියෙන්න ඕනේ:

```
ChatBot/
├── phi2/  ⬅️ Phi-2 model files මෙතන
├── all-MiniLM-L6-v2/  ⬅️ Embedding model files මෙතන
├── app.py
├── main.py
├── data/
└── ... (other files)
```

---

## 📥 Download කරන්නේ කොහොමද?

### **Method 1: HuggingFace (Recommended)**

#### 1️⃣ Phi-2 Model

**Download Link:**
```
https://huggingface.co/microsoft/phi-2
```

**Steps:**
1. HuggingFace site එකට යන්න
2. "Files and versions" tab එක click කරන්න
3. හැම file එකක්ම download කරන්න ඔන්න මේ files:
   - `config.json`
   - `model.safetensors` or `pytorch_model.bin`
   - `tokenizer.json`
   - `tokenizer_config.json`
   - `special_tokens_map.json`
   - `vocab.json`
   - `merges.txt`
   - සෙසු `.json` files

4. හැම files download වුනාම `C:\Users\damsara\Desktop\ChatBot\phi2\` folder එකක් හදලා ඒ ඇතුලට දාන්න

#### 2️⃣ all-MiniLM-L6-v2 Model

**Download Link:**
```
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
```

**Steps:**
1. HuggingFace site එකට යන්න
2. "Files and versions" tab එක click කරන්න
3. හැම file එකක්ම download කරන්න:
   - `config.json`
   - `pytorch_model.bin`
   - `tokenizer.json`
   - `tokenizer_config.json`
   - `vocab.txt`
   - සෙසු files

4. හැම files download වුනාම `C:\Users\damsara\Desktop\ChatBot\all-MiniLM-L6-v2\` folder එකක් හදලා ඒ ඇතුලට දාන්න

---

### **Method 2: Git LFS (Fast - හොඳම method)**

Git LFS install කරලා තියෙනවා නම් මේ විදියට download කරන්න පුළුවන්:

#### Install Git LFS (එක පාරක් විතරයි)
```bash
# Git LFS download කරන්න: https://git-lfs.github.com/
# Install කරලා restart terminal
```

#### Models Clone කරන්න
```bash
# Navigate to ChatBot folder
cd C:\Users\damsara\Desktop\ChatBot

# Download Phi-2
git clone https://huggingface.co/microsoft/phi-2

# Download all-MiniLM-L6-v2
git clone https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
```

---

### **Method 3: Python Script (Automatic)**

Python script එකකින් automatic download කරන්න:

#### 1. Hugging Face Hub Install කරන්න:
```bash
pip install huggingface_hub
```

#### 2. මේ script එක run කරන්න:

```python
# download_models.py
from huggingface_hub import snapshot_download
import os

# ChatBot folder path
chatbot_dir = r"C:\Users\damsara\Desktop\ChatBot"

print("📥 Downloading Phi-2 model...")
phi2_path = snapshot_download(
    repo_id="microsoft/phi-2",
    cache_dir=os.path.join(chatbot_dir, "phi2"),
    local_dir=os.path.join(chatbot_dir, "phi2"),
    local_dir_use_symlinks=False
)
print(f"✅ Phi-2 downloaded to: {phi2_path}")

print("\n📥 Downloading all-MiniLM-L6-v2 model...")
embedding_path = snapshot_download(
    repo_id="sentence-transformers/all-MiniLM-L6-v2",
    cache_dir=os.path.join(chatbot_dir, "all-MiniLM-L6-v2"),
    local_dir=os.path.join(chatbot_dir, "all-MiniLM-L6-v2"),
    local_dir_use_symlinks=False
)
print(f"✅ all-MiniLM-L6-v2 downloaded to: {embedding_path}")

print("\n🎉 සියලු models download වෙලා ඉවරයි!")
```

**Run කරන්න:**
```bash
python download_models.py
```

---

## ✅ හරියටම Download වුනාද Check කරන්නේ කොහොමද?

### Final Folder Structure:

```
C:\Users\damsara\Desktop\ChatBot\
│
├── phi2/
│   ├── config.json ✅
│   ├── model.safetensors (or pytorch_model.bin) ✅
│   ├── tokenizer.json ✅
│   ├── tokenizer_config.json ✅
│   ├── vocab.json ✅
│   └── ... (other files)
│
├── all-MiniLM-L6-v2/
│   ├── config.json ✅
│   ├── pytorch_model.bin ✅
│   ├── tokenizer.json ✅
│   ├── tokenizer_config.json ✅
│   ├── vocab.txt ✅
│   └── ... (other files)
│
├── app.py
├── main.py
└── ... (other project files)
```

### Check කරන්න PowerShell එකෙන්:

```powershell
# Check phi2 folder
Get-ChildItem "C:\Users\damsara\Desktop\ChatBot\phi2"

# Check all-MiniLM-L6-v2 folder
Get-ChildItem "C:\Users\damsara\Desktop\ChatBot\all-MiniLM-L6-v2"
```

තියෙන්න ඕනේ:
- ✅ `config.json` - Both folders එකේම
- ✅ `pytorch_model.bin` හෝ `model.safetensors` - Model weights
- ✅ `tokenizer` files - Tokenizer configs

---

## 💾 Model Sizes (Disk Space)

| Model | Size | Notes |
|-------|------|-------|
| **Phi-2** | ~5.5 GB | LLM model (text generation) |
| **all-MiniLM-L6-v2** | ~90 MB | Embeddings (search) |
| **Total** | ~5.6 GB | Make sure you have space! |

---

## 🚨 Common Issues

### Issue 1: "Models not found"
```
ERROR | Phi-2 model not found at: C:\...\phi2
```

**විසඳුම:**
- Folders නම් හරියටම තියෙනවද check කරන්න
- `phi2` (not `phi-2` or `Phi2`)
- `all-MiniLM-L6-v2` (exactly like this)

### Issue 2: Download වෙන්නේ නැහැ
- Internet connection check කරන්න
- HuggingFace site එක access කරන්න බැරි නම් VPN try කරන්න
- Git LFS install කරලා තියෙනවද check කරන්න

### Issue 3: Disk space නැහැ
- අවම වශයෙන් 6GB free space ඕනේ
- Disk cleanup කරන්න

---

## 🎯 Download කරලා ඉවරයි නං:

### 1. Verify Models:
```bash
# Run this to verify
python -c "import os; print('Phi-2:', os.path.exists('phi2/config.json')); print('Embeddings:', os.path.exists('all-MiniLM-L6-v2/config.json'))"
```

### 2. Test Run:
```bash
python app.py
```

Model files හරියටම තියෙනවා නම්:
```
✅ Phi-2 model loaded successfully!
✅ Embedding model loaded successfully!
```

Errors තියෙනවා නම්:
```
❌ Phi-2 model not found at: ...
```

---

## 📝 Quick Summary

**මොනවද කරන්න ඕනේ:**

1. **Models Download කරන්න:**
   - Phi-2: https://huggingface.co/microsoft/phi-2
   - all-MiniLM-L6-v2: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

2. **තියන්න ඕනේ:**
   - `C:\Users\damsara\Desktop\ChatBot\phi2\` (හැම files)
   - `C:\Users\damsara\Desktop\ChatBot\all-MiniLM-L6-v2\` (හැම files)

3. **Test කරන්න:**
   ```bash
   python app.py
   ```

---

## 🎉 Alternative: Online Models (If Download is Hard)

Models download කරන්න අමාරුනම්, OpenAI API හෝ Hugging Face API එකක් use කරන්න විකල්පයක් විදියට use කරන්න පුළුවන්. But මේ project එකෙන් අපේ අරමුණ **100% local** processing එක!

---

**Models download කළාට පස්සේ `python app.py` run කරන්න!** 🚀

ප්‍රශ්න තියෙනවා නම් මේ file එක reference කරන්න! 📖
