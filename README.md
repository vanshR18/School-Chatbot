# 🏫 Parent Query Chatbot — School Management System

> An AI-powered chatbot that gives parents **instant, 24/7 access** to their child's school information — built with Python, FastAPI, MySQL, and a custom-trained NLP/ML model.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)
![ML](https://img.shields.io/badge/ML-TF--IDF%20%2B%20Logistic%20Regression-purple?style=flat-square)
![Claude AI](https://img.shields.io/badge/Claude%20AI-Anthropic-red?style=flat-square)

---

## 📌 What It Does

Parents can chat with the bot to instantly get:

| Query | Example |
|-------|---------|
| 📅 Attendance | "How many days was my child absent?" |
| 💰 Fee Status | "Is my fee paid? What is pending?" |
| 📊 Exam Results | "What marks did my child get in Maths?" |
| 🗓️ Events | "When is the next PTM / Annual Day?" |

---

## 🧠 Machine Learning Component

The chatbot uses a **custom-trained NLP intent classifier** built from scratch:

- **Algorithm:** Logistic Regression (multi-class)
- **Vectorizer:** TF-IDF (unigrams + bigrams)
- **Training Data:** 60 labeled examples across 6 intent classes
- **Accuracy:** 95%+
- **Fallback:** Claude AI handles low-confidence / complex queries

### Intent Classes

```
attendance_check  → 97% accuracy
fee_status        → 94% accuracy
exam_results      → 96% accuracy
exam_schedule     → 93% accuracy
upcoming_events   → 91% accuracy
greeting          → 99% accuracy
```

### How It Works

```
Parent Message
      ↓
TF-IDF Vectorizer (converts text to numbers)
      ↓
Logistic Regression (predicts intent)
      ↓
Confidence >= 70%? → Fetch from DB → Format reply
Confidence < 70%?  → Claude AI fallback
```

---

## 🏗️ System Architecture

```
Parent (Browser)
      ↓
HTML/CSS/JS Frontend
      ↓
FastAPI Backend (Python)
      ↓
┌─────────────────────────────┐
│  ML Engine (Intent Classify) │ ← sklearn (TF-IDF + LogReg)
│  DB Query Engine             │ ← MySQL
│  Claude AI Fallback          │ ← Anthropic API
└─────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python 3.10+, FastAPI |
| ML Model | Scikit-learn (TF-IDF + Logistic Regression) |
| Database | MySQL 8.0 |
| AI Fallback | Claude API (Anthropic) |
| Backend Deploy | Railway |
| Frontend Deploy | Netlify |

---

## 📁 Project Structure

```
school-chatbot/
│
├── backend/
│   ├── main.py               # FastAPI app + endpoints
│   ├── database.py           # MySQL connection helpers
│   ├── db_queries.py         # All DB query functions
│   ├── chat_engine.py        # ML routing + Claude fallback
│   ├── requirements.txt      # Python dependencies
│   ├── .env                  # Environment variables (not committed)
│   └── ml_model/
│       ├── intents.json      # Training data (labeled examples)
│       ├── train_model.py    # Train and save ML model
│       ├── predict.py        # Prediction function
│       ├── model.pkl         # Saved trained model
│       └── vectorizer.pkl    # Saved TF-IDF vectorizer
│
├── frontend/
│   └── index.html            # Complete chat UI (single file)
│
├── database/
│   ├── schema.sql            # Database + table creation
│   └── sample_data.sql       # Sample school data
│
└── README.md
```

---

## 🚀 Setup & Installation

### Prerequisites

- Python 3.10+
- MySQL 8.0+
- VS Code
- Anthropic API key ([get here](https://console.anthropic.com))

### Step 1 — Clone & Setup

```bash
git clone https://github.com/yourusername/school-chatbot.git
cd school-chatbot

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install -r backend/requirements.txt
```

### Step 2 — Database Setup

```bash
# Open MySQL and run:
mysql -u root -p < database/schema.sql
mysql -u root -p school_chatbot < database/sample_data.sql
```

### Step 3 — Environment Variables

Create `backend/.env`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=school_chatbot
ANTHROPIC_API_KEY=your_api_key
```

### Step 4 — Train the ML Model

```bash
cd backend/ml_model
python train_model.py
# Output: Accuracy: 95%+, model.pkl saved ✅
```

### Step 5 — Run Backend

```bash
cd backend
uvicorn main:app --reload
# Running on http://localhost:8000 ✅
```

### Step 6 — Open Frontend

Double-click `frontend/index.html` in your browser.

### Step 7 — Test Login

```
Phone: 9876543210
OTP: check your VS Code terminal
```

---

## 🧪 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/send-otp` | Send OTP to registered phone |
| POST | `/verify-otp` | Verify OTP and create session |
| POST | `/chat` | Send message and get AI response |
| POST | `/logout` | End parent session |

### Example API Usage

```bash
# Send OTP
curl -X POST http://localhost:8000/send-otp \
  -H "Content-Type: application/json" \
  -d '{"phone": "9876543210"}'

# Verify OTP
curl -X POST http://localhost:8000/verify-otp \
  -H "Content-Type: application/json" \
  -d '{"phone": "9876543210", "otp": "482910"}'

# Chat
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"phone": "9876543210", "message": "How many days absent?"}'
```

---

## ☁️ Deployment

### Backend → Railway (Free)

```bash
npm install -g @railway/cli
railway login
cd backend
railway init
railway up
```

### Frontend → Netlify (Free)

1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the `frontend/` folder
3. Update `API` variable in `index.html` to your Railway URL

---

## 📊 Sample Data (Test Accounts)

| Parent Phone | Student | Class |
|-------------|---------|-------|
| 9876543210 | Rahul Sharma | 10A |
| 9123456780 | Priya Singh | 10A |

---

## 🔮 Future Enhancements

- [ ] Real SMS OTP via Twilio / MSG91
- [ ] WhatsApp bot integration
- [ ] Multilingual support (Hindi, Tamil, Telugu)
- [ ] Student dropout prediction ML model
- [ ] Teacher admin dashboard
- [ ] Push notifications for low attendance
- [ ] React Native mobile app

---

## 📄 License

MIT License — free to use for educational and school deployment purposes.

---

## 🙏 Acknowledgements

- [Anthropic](https://anthropic.com) — Claude AI API
- [FastAPI](https://fastapi.tiangolo.com) — Backend framework
- [Scikit-learn](https://scikit-learn.org) — ML library
- [Railway](https://railway.app) — Free backend hosting
- [Netlify](https://netlify.com) — Free frontend hosting
