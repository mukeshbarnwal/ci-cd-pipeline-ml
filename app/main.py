# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class InputText(BaseModel):
    text: str

HF_API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HEADERS = {"Authorization": "Bearer hf_XZQZQZQZQZQZQZQZQZQZQZQZQZQZQZQZ"}

@app.post("/predict")
def predict(input: InputText):
    payload = {"inputs": input.text}
    response = requests.post(HF_API_URL, headers=HEADERS, json=payload)
    result = response.json()
    return {"sentiment": result}
