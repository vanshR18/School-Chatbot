import pickle
import numpy as np
import os

# Load saved model
BASE = os.path.dirname(__file__)

with open(os.path.join(BASE, "model.pkl"), "rb") as f:
    model = pickle.load(f)

with open(os.path.join(BASE, "vectorizer.pkl"), "rb") as f:
    vectorizer = pickle.load(f)

def predict_intent(text):
    """
    Returns (intent, confidence)
    Example: ("attendance_check", 0.97)
    """
    vec = vectorizer.transform([text.lower()])
    intent = model.predict(vec)[0]
    confidence = model.predict_proba(vec).max()
    return intent, round(float(confidence), 2)

# Test it
if __name__ == "__main__":
    tests = [
        "How many days was my child absent?",
        "Is my fee paid?",
        "When is the next exam?",
        "What marks did my child get?",
        "Any upcoming events?",
        "Hello!",
        "Good morning",
        "Show attendance",
        "Fee pending?"
    ]
    print("\n🧪 Testing Intent Classifier:\n")
    for t in tests:
        intent, conf = predict_intent(t)
        print(f"  '{t}'")
        print(f"   → Intent: {intent} | Confidence: {conf*100:.0f}%\n")
