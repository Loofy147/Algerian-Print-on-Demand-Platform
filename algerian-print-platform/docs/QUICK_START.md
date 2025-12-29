# 🚀 QUICK START GUIDE
## Get Running in 30 Minutes

---

## Prerequisites

Before you begin, make sure you have:

```bash
# Required software
✅ Python 3.10+ installed
✅ Git installed
✅ Code editor (VS Code recommended)
✅ Terminal/Command line access

# Optional (for later)
⬜ Node.js 18+ (for frontend in Week 6)
⬜ PostgreSQL 15+ (for backend in Week 5)
⬜ Docker (optional, for production)
```

---

## Step 1: Repository Setup (5 minutes)

```bash
# 1. Create your repository
mkdir algerian-print-platform
cd algerian-print-platform

# 2. Initialize Git
git init
git branch -M main

# 3. Create repository on GitHub/GitLab
# Then add remote:
git remote add origin <your-repo-url>

# 4. Copy all files I created to this directory
# (Download from the outputs I'll provide)

# 5. First commit
git add .
git commit -m "Initial project structure"
git push -u origin main
```

---

## Step 2: ML Training Environment (10 minutes)

```bash
# 1. Go to https://kaggle.com
# 2. Create account (use your email)
# 3. Verify phone number (required for GPU access)
# 4. Go to Settings → Phone Verification

# 5. Check GPU quota
# Settings → Account → GPU Quota: 30 hours/week ✅

# 6. Create Hugging Face account
# Go to https://huggingface.co
# Sign up with email
# Settings → Access Tokens → New Token
# Save token securely (you'll need it for training)
```

---

## Step 3: Local Python Environment (10 minutes)

```bash
# 1. Navigate to ml-training folder
cd ml-training

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
# On Mac/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Test installation
python -c "import torch; print(f'PyTorch: {torch.__version__}')"
python -c "import diffusers; print('Diffusers installed ✅')"
```

---

## Step 4: Upload Notebooks to Kaggle (5 minutes)

```bash
# 1. Go to Kaggle.com
# 2. Click "Create" → "New Notebook"
# 3. Click "File" → "Import Notebook"
# 4. Upload: ml-training/notebooks/01_dataset_preparation.ipynb
# 5. Repeat for 02_flux_finetuning.ipynb

# OR use Kaggle API:
pip install kaggle
# Get API key from Kaggle → Settings → API → Create New API Token
kaggle kernels push -p ml-training/notebooks/
```

---

## Step 5: Start Dataset Collection (Ongoing)

Your first real task! Here's what to do today:

### A. Manual Collection (2-3 hours)

1. **Islamic Geometric Patterns**
   ```
   Search Google Images:
   - "Islamic geometric patterns" + Tools → Usage Rights → Creative Commons
   - Download 50-100 high-quality images
   - Save to: dataset/raw/geometric/
   ```

2. **Arabic Calligraphy**
   ```
   Search:
   - "Arabic calligraphy art"
   - "Islamic calligraphy design"
   - Download 50-100 images
   - Save to: dataset/raw/calligraphy/
   ```

3. **Algerian Cultural**
   ```
   Search:
   - "Algeria traditional patterns"
   - "Berber symbols"
   - "Algerian art"
   - Download 30-50 images
   - Save to: dataset/raw/cultural/
   ```

### B. Automated Collection

Use the dataset sources I mentioned:

1. **Wikimedia Commons**
   ```python
   # Use their API to download Islamic art
   # Example script in ml-training/scripts/download_wikimedia.py
   ```

2. **Museum APIs**
   ```python
   # Met Museum Open Access
   # British Museum
   # Scripts provided in ml-training/scripts/
   ```

---

## Your First Week Checklist

Print this out and check off as you go:

### Monday:
- [ ] Create Git repository
- [ ] Set up Kaggle account
- [ ] Set up Hugging Face account
- [ ] Upload notebooks to Kaggle

### Tuesday:
- [ ] Collect 200+ images (geometric + calligraphy)
- [ ] Organize into folders
- [ ] Test image quality

### Wednesday:
- [ ] Collect 200+ more images (cultural + modern)
- [ ] Start automated downloads
- [ ] Research Algerian artists for permission

### Thursday:
- [ ] Collect 200+ final images
- [ ] Total target: 600-1000 images minimum
- [ ] Upload to Kaggle as dataset

### Friday:
- [ ] Run dataset preparation notebook
- [ ] Process and clean images
- [ ] Generate captions

### Weekend:
- [ ] Review processed dataset
- [ ] Fix any issues
- [ ] Prepare for training next week

---

## Quick Commands Reference

```bash
# Check if Python installed
python --version

# Check if pip works
pip --version

# Create virtual environment
python -m venv venv

# Activate venv (Mac/Linux)
source venv/bin/activate

# Activate venv (Windows)
venv\Scripts\activate

# Install from requirements
pip install -r requirements.txt

# Deactivate venv
deactivate

# Check Git status
git status

# Commit changes
git add .
git commit -m "Your message"
git push
```

---

## Common Issues & Solutions

### Issue: "Python not found"
**Solution:**
```bash
# Install Python from python.org
# Or use package manager:
# Mac: brew install python
# Ubuntu: sudo apt install python3.10
```

### Issue: "pip install fails"
**Solution:**
```bash
# Upgrade pip
python -m pip install --upgrade pip

# Try with --user flag
pip install --user -r requirements.txt
```

### Issue: "No GPU on Kaggle"
**Solution:**
- Check you verified phone number
- Settings → Accelerator → GPU T4 x2
- Check GPU quota not exceeded

### Issue: "CUDA out of memory"
**Solution:**
- Reduce batch size in config
- Use gradient accumulation
- Restart notebook

---

## Next Steps After Setup

Once you complete the quick start:

1. **Read the full roadmap**
   - `docs/IMPLEMENTATION_ROADMAP.md`
   - Understand the 16-week plan

2. **Focus on Week 1 tasks**
   - Dataset collection is priority #1
   - Aim for 1,000+ images minimum

3. **Check in with me**
   - Share your progress
   - Ask questions when stuck
   - Show me your first dataset batch

---

## Resources

- **Project Documentation:** `docs/`
- **Training Notebooks:** `ml-training/notebooks/`
- **Backend Code:** `backend/`
- **Questions?** Ask me anytime!

---

## Emergency Contacts

When you're completely stuck:

1. **Ask Claude (me)** - I'm your partner, use me!
2. **Kaggle Forums** - For training issues
3. **Stack Overflow** - For code problems
4. **Discord/Reddit** - For community help

---

**Ready to build? Start with Step 1! 🚀**

Remember: Progress > Perfection. Just start, and we'll iterate together.
