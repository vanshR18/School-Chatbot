# 🏫 Parent Query Chatbot — School Management System

> An AI-powered chatbot that gives parents **instant, 24/7 access** to their child's school information — built with Python, FastAPI, MySQL, a custom-trained NLP/ML model, and a full Admin Dashboard.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green?style=flat-square&logo=fastapi)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?style=flat-square&logo=mysql)
![ML](https://img.shields.io/badge/ML-TF--IDF%20%2B%20Logistic%20Regression-purple?style=flat-square)
![Claude AI](https://img.shields.io/badge/Claude%20AI-Anthropic-red?style=flat-square)
![Admin](https://img.shields.io/badge/Admin-Dashboard-darkblue?style=flat-square)

---

## 📌 What It Does

### 👨‍👩‍👧 For Parents
Parents log in with OTP and chat with the bot to instantly get:

| Query | Example |
|-------|---------|
| 📅 Attendance | "How many days was my child absent?" |
| 💰 Fee Status | "Is my fee paid? What is pending?" |
| 📊 Exam Results | "What marks did my child get in Maths?" |
| 🗓️ Events | "When is the next PTM / Annual Day?" |

### 🏫 For School Admin
Admins use the dashboard to manage all school data without touching MySQL:

| Section | Actions |
|---------|---------|
| 📊 Dashboard | Live stats — students, attendance, fees, events |
| 👤 Students | Add new students, view all with phone numbers |
| 📅 Attendance | Click P/A/L per student and save in one click |
| 💰 Fees | Add records, mark payments as paid instantly |
| 📊 Results | Enter subject-wise marks per student |
| 🗓️ Events | Add PTM, exams, holidays — reflects in chatbot immediately |

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
Confidence >= 70%? → Fetch from DB → Format reply → return intent label
Confidence < 70%?  → Claude AI fallback → return "claude"
      ↓
Frontend shows ML badge (🧠 ML) or Claude badge (✨ Claude AI)
```

---

## 🏗️ System Architecture

```
Parent (Browser)              Admin (Browser)
      ↓                             ↓
frontend/index.html        frontend/admin.html
      ↓                             ↓
      └──────────┬──────────────────┘
                 ↓
        FastAPI Backend (Python)
                 ↓
   ┌─────────────────────────────────┐
   │  ML Engine (TF-IDF + LogReg)    │ ← predict intent
   │  DB Query Engine                │ ← fetch live MySQL data
   │  Admin Routes (/admin/*)        │ ← manage school data
   │  Claude AI Fallback             │ ← handle complex queries
   └─────────────────────────────────┘
                 ↓
           MySQL Database
    (students, attendance, fees,
      results, events tables)
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Parent Frontend | HTML5, CSS3, JavaScript (Dark theme UI) |
| Admin Frontend | HTML5, CSS3, JavaScript (Dark dashboard) |
| Backend | Python 3.10+, FastAPI |
| ML Model | Scikit-learn (TF-IDF + Logistic Regression) |
| Database | MySQL 8.0 |
| AI Fallback | Claude API (Anthropic) |
| Auth | OTP-based login (6-digit, 5 min expiry) |
| Backend Deploy | Railway |
| Frontend Deploy | Netlify |

---

## 📁 Project Structure

```
school-chatbot/
│
├── backend/
│   ├── main.py               # FastAPI app + all endpoints
│   ├── database.py           # MySQL connection helpers
│   ├── db_queries.py         # Parent chatbot DB queries
│   ├── chat_engine.py        # ML routing + Claude fallback (returns intent)
│   ├── admin_routes.py       # Admin panel API endpoints
│   ├── requirements.txt      # Python dependencies
│   ├── .env                  # Environment variables (not committed)
│   └── ml_model/
│       ├── intents.json      # Training data (60 labeled examples)
│       ├── train_model.py    # Train and save ML model
│       ├── predict.py        # Prediction function (returns intent + confidence)
│       ├── model.pkl         # Saved trained model
│       └── vectorizer.pkl    # Saved TF-IDF vectorizer
│
├── frontend/
│   ├── index.html            # Parent chat UI (OTP login + chat)
│   └── admin.html            # Admin dashboard (full data management)
│
├── database/
│   ├── schema.sql            # Creates all 5 tables
│   └── sample_data.sql       # 4 test students with full data
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
git clone https://github.com/vanshR18/school-chatbot.git
cd school-chatbot

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate      # Mac/Linux

# Install dependencies
pip install fastapi uvicorn mysql-connector-python python-dotenv anthropic scikit-learn
```

### Step 2 — Database Setup

```bash
# Open MySQL and run in order:
mysql -u root -p < database/schema.sql
mysql -u root -p school_chatbot < database/sample_data.sql
```

### Step 3 — Environment Variables

Create `backend/.env`:

```env
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=school_chatbot
ANTHROPIC_API_KEY=your_api_key_here
```

### Step 4 — Train the ML Model

```bash
cd backend/ml_model
python train_model.py
```

Expected output:
```
✅ Loaded 60 training samples
📊 Accuracy: 95%+
✅ Model saved: model.pkl
```

### Step 5 — Run Backend

```bash
cd backend
uvicorn main:app --reload
# Running on http://localhost:8000 ✅
```

### Step 6 — Open Frontend

```
Parent chatbot  →  double-click frontend/index.html
Admin dashboard →  double-click frontend/admin.html
```

### Step 7 — Test Login

```
Parent Chatbot:
  Phone: 9876543210
  OTP:   check your VS Code terminal

Admin Panel:
  Open admin.html directly — no login required
```

---

## 🧪 API Endpoints

### Parent Chatbot

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| POST | `/send-otp` | Send OTP to registered phone |
| POST | `/verify-otp` | Verify OTP and create session |
| POST | `/chat` | Send message → get reply + intent label |
| POST | `/logout` | End parent session |

### Admin Panel

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin/dashboard` | Live stats + recent data |
| GET | `/admin/students` | List all students |
| POST | `/admin/students/add` | Add new student |
| POST | `/admin/attendance/bulk` | Save attendance for all students |
| GET | `/admin/attendance/{id}` | View student attendance |
| GET | `/admin/fees` | Fee overview for all students |
| POST | `/admin/fees/add` | Add fee record |
| POST | `/admin/fees/mark-paid` | Mark fee as paid |
| POST | `/admin/results/add` | Add exam marks |
| GET | `/admin/results/{id}` | View student results |
| GET | `/admin/events` | List upcoming events |
| POST | `/admin/events/add` | Add new event |

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

# Chat (response includes intent label)
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"phone": "9876543210", "message": "How many days absent?"}'

# Response:
# { "reply": "📅 Attendance Report...", "intent": "attendance_check" }
```

---

## 📊 Sample Data (Test Accounts)

| Parent Phone | Student | Class | Notes |
|-------------|---------|-------|-------|
| 9876543210 | Rahul Sharma | 10A | 3 absences, April fee pending |
| 9123456780 | Priya Singh | 10A | 1 absence, all fees paid |
| 9988776655 | Amit Verma | 10B | 2 absences, 3 months fee pending |
| 9871234560 | Sneha Gupta | 10B | Perfect attendance, all fees paid |

---

## ☁️ Deployment

### Backend → Railway (Free)

```bash
npm install -g @railway/cli
railway login
cd backend
railway init
railway up
# You get a URL like: https://school-chatbot-backend.up.railway.app
```

### Frontend → Netlify (Free)

1. Go to [netlify.com](https://netlify.com)
2. Drag and drop the `frontend/` folder
3. Update `const API` in both `index.html` and `admin.html`:

```javascript
// Change this in BOTH files:
const API = "http://localhost:8000";
// To your Railway URL:
const API = "https://your-app.up.railway.app";
```

---

## 🔁 How Live Data Works

Any data added via the Admin Panel reflects in the parent chatbot **instantly** — no restart needed:

```
Admin marks attendance  →  MySQL updates  →  Parent chatbot shows it  ✅
Admin marks fee paid    →  MySQL updates  →  Parent sees it as paid   ✅
Admin adds exam marks   →  MySQL updates  →  Results appear in chat   ✅
Admin adds school event →  MySQL updates  →  Event shows in chatbot   ✅
```

---

## 🔮 Future Enhancements

- [ ] Real SMS OTP via Twilio / MSG91
- [ ] WhatsApp bot integration
- [ ] Multilingual support (Hindi, Tamil, Telugu)
- [ ] Student dropout prediction ML model
- [ ] Push notifications for low attendance alerts
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
