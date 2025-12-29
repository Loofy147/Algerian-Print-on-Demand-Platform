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
│   │   ├── models/         # Database models
│   │   ├── services/       # Business logic
│   │   └── ml/             # ML inference
│   ├── tests/
│   └── requirements.txt
│
├── frontend/               # Next.js frontend
│   ├── src/
│   │   ├── app/           # App router pages
│   │   ├── components/    # React components
│   │   ├── lib/           # Utilities
│   │   └── styles/        # CSS/Tailwind
│   ├── public/
│   └── package.json
│
├── ml-training/           # Model training
│   ├── notebooks/         # Kaggle/Colab notebooks
│   ├── scripts/           # Training scripts
│   ├── configs/           # Training configs
│   └── datasets/          # Dataset processing
│
├── infrastructure/        # Deployment configs
│   ├── docker/
│   ├── kubernetes/
│   └── terraform/
│
├── docs/                  # Documentation
│   ├── api/
│   ├── deployment/
│   └── guides/
│
└── scripts/              # Utility scripts
    ├── setup/
    └── deploy/
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker (optional)
- PostgreSQL 15+
- Redis 7+

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # Configure your environment
uvicorn app.main:app --reload
```

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env.local  # Configure your environment
npm run dev
```

### ML Training Setup
```bash
cd ml-training
pip install -r requirements.txt
# Follow notebooks/README.md for Kaggle setup
```

## 📅 Development Roadmap

### Phase 1: Foundation (Weeks 1-4)
- [x] Project setup and repository structure
- [ ] Dataset collection and curation (10K images)
- [ ] Initial Flux fine-tuning on Kaggle
- [ ] Backend API structure
- [ ] Frontend design system

### Phase 2: Core Features (Weeks 5-8)
- [ ] Design generation API
- [ ] Product customization UI
- [ ] Order management system
- [ ] Payment integration (CIB, COD)
- [ ] Local print partner integration

### Phase 3: Beta Launch (Weeks 9-12)
- [ ] User authentication and profiles
- [ ] Design gallery and templates
- [ ] Order tracking
- [ ] Admin dashboard
- [ ] Beta testing with 100 users

### Phase 4: Public Launch (Weeks 13-16)
- [ ] Marketing website
- [ ] Production deployment
- [ ] Analytics and monitoring
- [ ] Customer support system
- [ ] Public launch campaign

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for PostgreSQL
- **Celery** - Async task queue
- **Redis** - Caching and sessions
- **Pydantic** - Data validation

### Frontend
- **Next.js 14** - React framework with App Router
- **TypeScript** - Type safety
- **Tailwind CSS** - Styling with RTL support
- **Shadcn/ui** - UI component library
- **React Query** - Data fetching

### ML/AI
- **Flux** - Base model for image generation
- **Diffusers** - Hugging Face library
- **PyTorch** - Deep learning framework
- **LoRA** - Efficient fine-tuning
- **vLLM** - Fast inference serving

### Infrastructure
- **Docker** - Containerization
- **PostgreSQL** - Primary database
- **Redis** - Cache and queue
- **MinIO** - Object storage (S3-compatible)
- **Nginx** - Reverse proxy

## 🔐 Security

- JWT authentication
- Rate limiting on all endpoints
- Input validation and sanitization
- HTTPS only in production
- Secure payment handling
- Content moderation for generated images

## 🌍 Localization

- Arabic-first interface (RTL support)
- French secondary language
- Algerian Dinar (DZD) pricing
- Local date/time formats
- Cultural design patterns

## 📊 Key Features

### For Customers
- ✅ AI-powered design generation
- ✅ Arabic calligraphy support
- ✅ Cultural pattern library
- ✅ Real-time product mockups
- ✅ Cash on delivery
- ✅ Fast local shipping

### For Business
- ✅ Order management dashboard
- ✅ Inventory tracking
- ✅ Analytics and reporting
- ✅ Print partner integration
- ✅ Customer communication tools

## 🤝 Contributing

This is a private project in active development. Team members, please follow:
- Git flow branching strategy
- Code review requirements
- Testing standards
- Documentation requirements

## 📝 License

Proprietary - All rights reserved

## 📧 Contact

For questions or support, contact the development team.

---

**Built with ❤️ for the Algerian market**
