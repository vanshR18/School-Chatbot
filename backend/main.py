from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from db_queries import get_student_by_phone
from chat_engine import get_bot_response
import random
import time

load_dotenv()

app = FastAPI(title="School Chatbot API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Import admin routes
try:
    from admin_routes import admin_router
    app.include_router(admin_router)
    print("✅ Admin routes loaded")
except Exception as e:
    print(f"⚠️ Admin routes not loaded: {e}")

# Session + OTP store
sessions = {}
otp_store = {}

class PhoneRequest(BaseModel):
    phone: str

class OTPRequest(BaseModel):
    phone: str
    otp: str

class ChatRequest(BaseModel):
    phone: str
    message: str

@app.get("/")
def root():
    return {"status": "✅ School Chatbot API is running"}

# ── STEP 1: Send OTP ──
@app.post("/send-otp")
def send_otp(req: PhoneRequest):
    student = get_student_by_phone(req.phone)
    if not student:
        raise HTTPException(status_code=404, detail="Phone not registered. Contact school office.")

    otp = str(random.randint(100000, 999999))
    otp_store[req.phone] = {
        "otp": otp,
        "expires_at": time.time() + 300  # 5 min expiry
    }

    # Print to terminal (replace with SMS API for production)
    print(f"\n📱 OTP for {req.phone}: {otp}\n")

    return {"message": "OTP sent successfully", "student_name": student['name']}

# ── STEP 2: Verify OTP ──
@app.post("/verify-otp")
def verify_otp(req: OTPRequest):
    record = otp_store.get(req.phone)

    if not record:
        raise HTTPException(status_code=400, detail="OTP not requested. Please send OTP first.")
    if time.time() > record['expires_at']:
        raise HTTPException(status_code=400, detail="OTP expired. Please request a new one.")
    if record['otp'] != req.otp:
        raise HTTPException(status_code=400, detail="Wrong OTP. Please try again.")

    student = get_student_by_phone(req.phone)
    sessions[req.phone] = student
    del otp_store[req.phone]

    return {
        "success": True,
        "message": f"Welcome {student['parent_name']}!",
        "student_name": student['name'],
        "class": student['class']
    }

# ── STEP 3: Chat — now returns intent too ──
@app.post("/chat")
def chat(req: ChatRequest):
    if req.phone not in sessions:
        raise HTTPException(status_code=401, detail="Session expired. Please login again.")

    student = sessions[req.phone]

    # get_bot_response now returns (reply, intent) tuple
    reply, intent = get_bot_response(req.message, student['name'], student['id'])

    return {
        "reply": reply,
        "intent": intent   # ← sent to frontend to show ML badge
    }

# ── STEP 4: Logout ──
@app.post("/logout")
def logout(req: PhoneRequest):
    sessions.pop(req.phone, None)
    return {"message": "Logged out successfully"}