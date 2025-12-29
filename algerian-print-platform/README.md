# 🇩🇿 Algerian Print-on-Demand Platform

AI-powered custom merchandise platform for the Algerian market, featuring Arabic-first design tools and local fulfillment.

## 🎯 Project Vision

Enable Algerians to create custom t-shirts, mugs, and merchandise using AI-generated designs that understand North African culture, Arabic calligraphy, and local aesthetics.

## 🏗️ Architecture

```
┌─────────────────────────────────────────┐
│         Next.js Frontend (Arabic)        │
│  Product Designer + Order Management     │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│        FastAPI Backend (Python)          │
│  Orders + Payments + User Management     │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│      Fine-Tuned Flux Model (Algerian)    │
│   Arabic designs + Cultural patterns     │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│      Print Fulfillment (Hybrid)          │
│   Local Partners + EU Backup             │
└─────────────────────────────────────────┘
```

## 📦 Repository Structure

```
algerian-print-platform/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── api/            # API endpoints
│   │   ├── core/           # Config, security
│   │   ├── crud/           # Database operations
│   │   ├── db/             # Database session
│   │   ├── models/         # Database models
│   │   ├── schemas/        # Pydantic schemas
│   │   └── main.py
│   ├── alembic/            # Database migrations
│   ├── tests/
│   └── requirements.txt
│
├── frontend/               # Next.js frontend
│   └── (To be created)
│
├── ml-training/           # Model training
│   ├── notebooks/
│   ├── scripts/
│   └── datasets/
│
└── docs/                  # Project documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+ (for frontend)
- Docker
- PostgreSQL 15+

### Backend Setup
```bash
# 1. Navigate to the backend directory
cd backend

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up the database
# (Make sure you have PostgreSQL running)
createdb algerian_print

# 5. Create a .env file from the example
cp .env.example .env
# (Update .env with your database URL and a strong SECRET_KEY)

# 6. Run database migrations
alembic upgrade head

# 7. Run the development server
uvicorn app.main:app --reload
```
The API will be available at `http://localhost:8000`.

### ML Training Setup
```bash
cd ml-training
pip install -r requirements.txt
# Follow the guides in the notebooks for Kaggle setup.
```

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for PostgreSQL
- **Alembic** - Database migrations
- **Pydantic** - Data validation
- **Passlib** - Password hashing
- **python-jose** - JWT implementation

### And more... (Full stack details in the original README)
