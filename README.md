# Parent Query Chatbot - Full Project Plan

## 🎯 Project Overview

A chatbot that answers parent queries about their child's school information via a web interface — pulling real data like attendance, fees, exam schedules, and results.

---

## 🏗️ System Architecture

```
Parent (Web/WhatsApp)
        ↓
   Chat Interface
        ↓
   NLP Engine (Intent Detection)
        ↓
   Query Handler
        ↓
   School Database
        ↓
   Response Generator
        ↓
   Parent gets answer
```

---

## 📋 What It Can Answer

| Category | Example Questions |
|---|---|
| 📅 Attendance | "How many days was Rahul absent this month?" |
| 💰 Fees | "Is my fee due? How much is pending?" |
| 📝 Exams | "When is the next exam?" "What are the exam subjects?" |
| 📊 Results | "What marks did my child get in Math?" |
| 🏫 Events | "When is the annual day?" "Is school open on Friday?" |
| 🚌 Transport | "What time does the bus arrive?" |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | React.js or plain HTML/CSS |
| Backend | Python (FastAPI or Flask) |
| NLP / AI | Claude API (intent detection + response) |
| Database | MySQL or SQLite |
| Authentication | OTP login via phone number |
| Hosting | Railway / Render (free) |

---

## 🗂️ Project Folder Structure

```
school-chatbot/
│
├── frontend/
│   ├── index.html
│   ├── chat.js
│   └── style.css
│
├── backend/
│   ├── main.py              # FastAPI app
│   ├── intent_handler.py    # Classifies user query
│   ├── db_queries.py        # Fetches data from DB
│   ├── response_builder.py  # Formats final reply
│   └── auth.py              # Parent login/OTP
│
├── database/
│   ├── schema.sql           # DB structure
│   └── sample_data.sql      # Dummy school data
│
├── ml_model/
│   ├── train_intent.py      # Train intent classifier
│   ├── intents.json         # Intent training data
│   └── model.pkl            # Saved model
│
└── requirements.txt
```

---

## 🧠 How the NLP Works

### Step 1 — Intent Detection
Classify what the parent is asking:

```
"When is Rahul's exam?"  →  intent: exam_schedule
"How much fee is due?"   →  intent: fee_status
"Was Priya absent today?"→  intent: attendance_check
```

### Step 2 — Entity Extraction
Pull out key details:
```
"How many days was Rahul absent in January?"
  → student_name: Rahul
  → month: January
  → intent: attendance_check
```

### Step 3 — Database Query
```python
def get_attendance(student_name, month):
    query = """
        SELECT COUNT(*) as absent_days 
        FROM attendance 
        WHERE student_name = %s 
        AND MONTH(date) = %s 
        AND status = 'Absent'
    """
    return db.execute(query, (student_name, month))
```

### Step 4 — Generate Response
```
"Rahul was absent 3 days in January. 
 Total school days: 22. Attendance: 86%"
```

---

## 🗃️ Database Schema

```sql
-- Students Table
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    class VARCHAR(10),
    parent_phone VARCHAR(15),
    roll_number VARCHAR(20)
);

-- Attendance Table
CREATE TABLE attendance (
    id INT PRIMARY KEY,
    student_id INT,
    date DATE,
    status ENUM('Present', 'Absent', 'Late'),
    FOREIGN KEY (student_id) REFERENCES students(id)
);

-- Fees Table
CREATE TABLE fees (
    id INT PRIMARY KEY,
    student_id INT,
    month VARCHAR(20),
    amount DECIMAL(10,2),
    paid BOOLEAN,
    due_date DATE
);

-- Exam Results Table
CREATE TABLE results (
    id INT PRIMARY KEY,
    student_id INT,
    subject VARCHAR(50),
    exam_type VARCHAR(30),
    marks_obtained INT,
    total_marks INT,
    exam_date DATE
);

-- Events Table
CREATE TABLE events (
    id INT PRIMARY KEY,
    event_name VARCHAR(100),
    event_date DATE,
    description TEXT
);
```

---

## 🔐 Parent Authentication Flow

```
1. Parent opens chatbot
2. Enters registered mobile number
3. Receives OTP (via SMS / WhatsApp)
4. Logs in → session created
5. Chatbot knows which student to fetch data for
6. All queries are auto-linked to their child
```

---

## 💬 Sample Conversation Flow

```
🤖 Bot: Hello! I'm your school assistant. 
        How can I help you today?

👤 Parent: How many days was my son absent?

🤖 Bot: Arjun has been absent 4 days this month 
        (March 2026). 
        Days missed: Mar 3, 7, 11, 19
        Current attendance: 78% ⚠️
        Minimum required: 75%

👤 Parent: Is my fee paid?

🤖 Bot: ✅ March fee: PAID (₹4,500)
        ❌ April fee: PENDING (₹4,500)
        Due date: April 5, 2026

👤 Parent: When is the next exam?

🤖 Bot: 📝 Unit Test 2 Schedule:
        • Math    → April 10
        • Science → April 11  
        • English → April 12
        • Hindi   → April 13
        Syllabus notice was sent on March 1.
```

---

## 📅 Development Timeline

| Week | Task |
|---|---|
| Week 1 | Design DB schema + insert sample data |
| Week 2 | Build backend API (FastAPI) + DB queries |
| Week 3 | Train intent classifier + entity extractor |
| Week 4 | Build chat frontend (React or HTML) |
| Week 5 | Connect frontend ↔ backend ↔ DB |
| Week 6 | Add OTP login + session management |
| Week 7 | Testing, bug fixes, edge cases |
| Week 8 | Deploy + demo to school management |

---

## 📊 ML Component (Intent Classifier)

```python
# intents.json sample
{
  "intents": [
    {
      "tag": "attendance_check",
      "patterns": [
        "How many days absent?",
        "What is attendance this month?",
        "Was my child present today?",
        "Show me attendance report"
      ]
    },
    {
      "tag": "fee_status",
      "patterns": [
        "Is fee paid?",
        "How much fee is pending?",
        "What is due amount?",
        "Fee payment status"
      ]
    },
    {
      "tag": "exam_schedule",
      "patterns": [
        "When is the exam?",
        "What subjects are in exam?",
        "Exam timetable",
        "Next test date"
      ]
    }
  ]
}
```

**Train with:** `sklearn` (TF-IDF + Logistic Regression) or use Claude API directly for intent detection — much more accurate.

---

## 🚀 Future Upgrades

- **WhatsApp Integration** via Twilio API
- **Multilingual support** (Hindi, regional languages)
- **Push notifications** for low attendance alerts
- **Voice input** support
- **Teacher-side dashboard** to push announcements into bot

---

