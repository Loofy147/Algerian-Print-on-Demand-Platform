# 🚀 QUICK START GUIDE
## Get Running in 30 Minutes

---

## Prerequisites

Make sure you have the following installed:
- Python 3.10+
- Git
- PostgreSQL 15+
- Docker (optional, for production)

---

## Step 1: Repository & ML Environment Setup (15 minutes)

```bash
# 1. Clone your repository (or set it up if you haven't)
git clone <your-repo-url>
cd algerian-print-platform

# 2. Set up the ML training environment
cd ml-training
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# 3. Verify ML environment
python -c "import torch; print('PyTorch OK')"
```

---

## Step 2: Backend Setup (15 minutes)

This will get your local API server running.

```bash
# 1. Navigate to the backend directory
cd ../backend  # Assumes you are in the ml-training directory

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install backend dependencies
pip install -r requirements.txt

# 4. Create your local database
# (Ensure PostgreSQL is running)
createdb algerian_print

# 5. Configure your environment
# Copy the example .env file
cp .env.example .env

# Open .env and set your DATABASE_URL if it's different.
# IMPORTANT: Change the SECRET_KEY to a new, random string.
# You can generate one with: openssl rand -hex 32

# 6. Set up and run database migrations
# (This will create the initial database tables)
alembic init alembic
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

# 7. Start the server
uvicorn app.main:app --reload
```
Your API should now be running at `http://localhost:8000`. You can visit this URL in your browser to see the health check (`{"status": "ok"}`).

---

## Step 3: Kaggle & Hugging Face (10 minutes)

If you plan to train the model, set up these accounts:

1.  **Kaggle:**
    *   Create an account at `https://kaggle.com`.
    *   **Verify your phone number** to get GPU access.
    *   Upload the notebooks from the `ml-training/notebooks` directory.

2.  **Hugging Face:**
    *   Create an account at `https://huggingface.co`.
    *   Generate an access token with "write" permissions. You'll need this to save your trained models.

---

## Next Steps

With the backend running, you are now ready to:

1.  **Run the dataset collection script:**
    ```bash
    cd ../ml-training
    python scripts/download_data.py
    ```

2.  **Explore the API documentation:**
    *   With the server running, visit `http://localhost:8000/docs` to see the interactive FastAPI documentation.

3.  **Read the full `IMPLEMENTATION_ROADMAP.md`** to understand the week-by-week plan for building the rest of the platform.

---
