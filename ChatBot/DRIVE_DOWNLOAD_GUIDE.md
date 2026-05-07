# 📤 Models Drive එකේ තියලා Download කරන්නේ කොහොමද

## ✅ ඔව්, මේක වැඩ කරනවා!

Models Google Drive, OneDrive, Dropbox වගේ cloud storage එකක upload කරලා public links share කරන්න පුළුවන්!

---

## 🔗 **Ready-to-Download Model Links** ⚡

**Models මේ links වලින් download කරගන්න පුළුවන්:**

### 1️⃣ **Phi-2 Model** (5.5GB) - Main LLM
```
https://drive.google.com/drive/folders/1FYV7cXBjYf1lAKIGdiRQ7zmB_9iGvCc8?usp=sharing
```
- **Folder Name:** `phi2`
- **Place In:** `ChatBot/phi2/`

### 2️⃣ **all-MiniLM-L6-v2** (90MB) - Embedding Model
```
https://drive.google.com/drive/folders/1OwrkNzx8wNssvq9kcIU9I8fH4-7_cH1C?usp=sharing
```
- **Folder Name:** `all-MiniLM-L6-v2`
- **Place In:** `ChatBot/all-MiniLM-L6-v2/`

### 📥 **Download කරන්න:**
1. Link එක click කරන්න
2. Folder එක right-click → **"Download"**
3. ZIP file එක extract කරන්න
4. `ChatBot` folder එකට copy කරන්න

**Scroll down for detailed download methods** (browser, gdown, PowerShell)

---

## 📤 Models Upload කරන්න (Drive එකට)

### **Option 1: Google Drive (Recommended)**

#### Step 1: Models Upload කරන්න
1. **Google Drive** එකට යන්න (drive.google.com)
2. **"New"** → **"Folder upload"** click කරන්න
3. `phi2` folder එක select කරන්න → Upload
4. `all-MiniLM-L6-v2` folder එක select කරන්න → Upload

#### Step 2: Public Links හදන්න

**Phi-2 Link:**
1. Drive එකේ `phi2` folder එක right-click කරන්න
2. **"Share"** click කරන්න
3. **"Change to anyone with the link"** click කරන්න
4. Permission: **"Viewer"** තියන්න
5. **"Copy link"** - මේක save කරගන්න!

**all-MiniLM-L6-v2 Link:**
1. Drive එකේ `all-MiniLM-L6-v2` folder එක right-click කරන්න
2. Same steps - Share → Anyone with link → Copy link

#### Step 3: Links Test කරන්න
- Links incognito window එකක open කරලා බලන්න accessible දැයි

---

### **Option 2: OneDrive**

1. OneDrive එකට models upload කරන්න
2. Folder එක right-click → **"Share"**
3. **"Anyone with the link can view"** select කරන්න
4. **"Copy link"**

---

### **Option 3: Dropbox**

1. Dropbox එකට models upload කරන්න
2. Folder hover කරලා **"Share"** click කරන්න
3. **"Create link"** → **"Anyone with the link"**
4. Link copy කරන්න

---

## 📥 Drive Links වලින් Download කරන්නේ කොහොමද?

### **Method 1: Manual Download (Browser)**

**Google Drive Links නම්:**

```
https://drive.google.com/drive/folders/YOUR_FOLDER_ID
```

1. Link එක browser එකෙන් open කරන්න
2. Folder එක right-click → **"Download"**
3. ZIP file එකක් download වෙනවා
4. Extract කරන්න
5. `C:\Users\damsara\Desktop\ChatBot\` folder එකට copy කරන්න

---

### **Method 2: gdown (Python - Automatic)**

Google Drive වලින් direct download කරන්න Python script එකක් use කරන්න පුළුවන්:

#### Install gdown:
```bash
pip install gdown
```

#### Download කරන්න:

```python
# download_from_drive.py
import gdown
import os

# Your Google Drive folder IDs (links වලින් extract කරන්න)
PHI2_FOLDER_ID = "YOUR_PHI2_FOLDER_ID"  # Link එකේ /folders/ පස්සේ තියෙන ID එක
EMBEDDING_FOLDER_ID = "YOUR_EMBEDDING_FOLDER_ID"

# ChatBot folder
chatbot_dir = r"C:\Users\damsara\Desktop\ChatBot"

print("📥 Downloading Phi-2 from Google Drive...")
# Download folder as zip
gdown.download_folder(
    id=PHI2_FOLDER_ID,
    output=os.path.join(chatbot_dir, "phi2"),
    quiet=False,
    use_cookies=False
)

print("📥 Downloading all-MiniLM-L6-v2 from Google Drive...")
gdown.download_folder(
    id=EMBEDDING_FOLDER_ID,
    output=os.path.join(chatbot_dir, "all-MiniLM-L6-v2"),
    quiet=False,
    use_cookies=False
)

print("✅ Download complete!")
```

**Run කරන්න:**
```bash
python download_from_drive.py
```

---

### **Method 3: Direct Download Script (PowerShell)**

Google Drive direct link එකක් use කරලා download කරන්න:

```powershell
# Download Phi-2
$phi2Url = "YOUR_GOOGLE_DRIVE_DIRECT_DOWNLOAD_LINK"
$phi2Zip = "C:\Users\damsara\Desktop\ChatBot\phi2.zip"

Write-Host "📥 Downloading Phi-2..."
Invoke-WebRequest -Uri $phi2Url -OutFile $phi2Zip

Write-Host "📦 Extracting Phi-2..."
Expand-Archive -Path $phi2Zip -DestinationPath "C:\Users\damsara\Desktop\ChatBot\" -Force
Remove-Item $phi2Zip

Write-Host "✅ Phi-2 downloaded!"

# Same for all-MiniLM-L6-v2
```

---

## 🔗 Google Drive Link වලින් Folder ID එක හොයාගන්නේ කොහොමද?

Link එක මෙහෙම තියෙනවා නම්:
```
https://drive.google.com/drive/folders/1A2B3C4D5E6F7G8H9
```

**Folder ID = `1A2B3C4D5E6F7G8H9`**

මේක copy කරලා Python script එකේ use කරන්න.

---

## 📋 Share කරන්න බොහොම ලේසියි!

### **README එකට Links එකතු කරන්න:**

```markdown
## 📥 Model Downloads

Models තියෙන්නේ Google Drive එකේ:

### Phi-2 Model
**Download:** [Google Drive Link](https://drive.google.com/drive/folders/YOUR_PHI2_FOLDER_ID)

**Place in:** `ChatBot/phi2/`

### all-MiniLM-L6-v2 Model
**Download:** [Google Drive Link](https://drive.google.com/drive/folders/YOUR_EMBEDDING_FOLDER_ID)

**Place in:** `ChatBot/all-MiniLM-L6-v2/`

---

### Quick Setup:
1. Download both folders from above links
2. Extract if zipped
3. Place in ChatBot folder
4. Run: `python app.py`
```

---

## 🎯 Benefits (වාසි):

### ✅ Advantages:
1. **ඉක්මන් download** - HuggingFace වලට වඩා fast
2. **කෙනෙකුට links share කරන්න පුළුවන්** - Team members, friends
3. **Multiple devices** - ඕනෑම device එකකින් download කරන්න පුළුවන්
4. **Reliable** - Google Drive/OneDrive stable
5. **No HuggingFace account** - Account එකක් ඕනේ නැහැ

### ⚠️ Considerations:
1. **Storage quota** - Google Drive free tier එකේ 15GB (Phi-2 5.5GB නිසා fit වෙනවා)
2. **Large files** - Drive එකෙන් download කරනකොට bandwidth limits තියෙන්න පුළුවන්
3. **Zip files** - Large folders download කරනකොට zip එකක් වෙලා download වෙනවා

---

## 🚀 Complete Workflow Example:

### **For You (Uploader):**

```bash
# 1. Models තියෙනවා නම් upload කරන්න
# - Google Drive open කරන්න
# - phi2 folder upload කරන්න
# - all-MiniLM-L6-v2 folder upload කරන්න

# 2. Public links හදන්න
# - Each folder → Share → Anyone with link → Viewer
# - Copy links

# 3. Links share කරන්න (README.md එකේ දාන්න)
```

### **For Others (Downloaders):**

```bash
# 1. Links click කරන්න
# 2. Download කරන්න (ZIP එකක් download වෙනවා)
# 3. Extract කරන්න
# 4. ChatBot folder එකට move කරන්න

# Example:
# Downloaded: phi2.zip
# Extract to: C:\Users\damsara\Desktop\ChatBot\phi2\

# 5. Run
python app.py
```

---

## 💡 Pro Tips:

### 1. **Folder Structure ඕනේ හරියටම:**

Extracted කළාම folder structure මෙහෙම තියෙන්න ඕනේ:

```
ChatBot/
├── phi2/  ← folder එක (not phi2.zip or phi2/phi2/)
│   ├── config.json
│   ├── model.safetensors
│   └── ... (files directly here)
│
├── all-MiniLM-L6-v2/  ← folder එක
│   ├── config.json
│   ├── pytorch_model.bin
│   └── ... (files directly here)
```

**Common mistake:** ZIP extract කරනකොට nested folders හදනවා:
```
❌ Wrong: ChatBot/phi2/phi2/config.json
✅ Correct: ChatBot/phi2/config.json
```

### 2. **Download Speed වැඩි කරන්න:**

- **IDM** (Internet Download Manager) use කරන්න
- **Browser extensions** - Downloader extensions
- **Google Drive Desktop** - Sync කරන්න direct

### 3. **Multiple Parts වලට split කරන්න:**

Phi-2 ලොකු නිසා parts වලට split කරලා upload කරන්න පුළුවන්:

**Windows:**
```powershell
# Split into 2GB parts
$source = "phi2.zip"
$destPattern = "phi2.zip.part"
$partSize = 2GB

# Then upload each part separately
```

---

## 📝 Updated README Section:

මේක ඔයාගේ README.md එකට add කරන්න:

```markdown
## 📥 Quick Model Download (Google Drive)

Models HuggingFace වලින් download කරන්න අමාරු නම්, මේ Google Drive links use කරන්න:

### Downloads:
- **Phi-2 Model:** [Download from Google Drive](YOUR_LINK_HERE) (~5.5 GB)
- **all-MiniLM-L6-v2:** [Download from Google Drive](YOUR_LINK_HERE) (~90 MB)

### Instructions:
1. Click links above → Download folders
2. Extract ZIP files (if downloaded as ZIP)
3. Place in ChatBot folder:
   - `phi2/` → `ChatBot/phi2/`
   - `all-MiniLM-L6-v2/` → `ChatBot/all-MiniLM-L6-v2/`
4. Run: `python app.py`

**Note:** Make sure folder structure is correct (files should be directly inside folders).
```

---

## ✅ Verification After Download:

```powershell
# Check if models downloaded correctly
Get-ChildItem "C:\Users\damsara\Desktop\ChatBot\phi2"
Get-ChildItem "C:\Users\damsara\Desktop\ChatBot\all-MiniLM-L6-v2"

# Should see config.json and other files (not nested folders)
```

---

## 🎉 Ready to Go!

1. ✅ Models upload කරන්න Drive එකට
2. ✅ Public links හදන්න
3. ✅ Links README.md එකේ දාන්න
4. ✅ Anyone can download and use!

---

**මේ method එක හොඳම එක වෙන්න පුළුවන් team projects වලට හෝ models බාගත කරන්න අමාරු තැන්වල!** 🚀

ප්‍රශ්න තියෙනවා නම් කියන්න! 😊
