# app.py - This is your API brain
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import os 

app = FastAPI(title="IVOMA AI API")

#Put your key here
GEMINI_KEY = os.getenv("GEMINI_KEY,", "PASTE_YOUR_KEY_HERE")

class ChatRequest(BaseModel):
    message: str
    history: list = []

@app.get("/") 
def home():
    return {"status": "IVOMA AI API is running"} 
@app.post("/chat")
def chat(req: ChatRequest):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key{GEMINI_KEY}"

    prompt = f"""
    You are IVOMA AI - Intelligence that Works for You.
    Give user exactly what they want. If code, give code. If feedback, give feedback.
    History: {req.history[-5:]}
    User: {req.message}
    """

    body = {"contents": [{"parts": [{"text": prompt}]}]}
    r = requests.post(url, json=body, timeout=30)
    data = r.json()
    reply = data['candinates'][0]['content']['parts'][0]['text']

    returrn {"reply": reply, "status": "success"}

# Run with: uvicorn app:app --host 0.0.0.0 --port 8000    


    