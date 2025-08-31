# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import requests
import uvicorn
from openai import OpenAI
import enum
from enum import Enum
import instructor
app = FastAPI()
class InputText(BaseModel):
    text: str

class ComplaintCategory(str, Enum):
    product = "Product"
    finance = "Finance"
    shipping = "Shipping"
    customer_service = "CustomerService"

class OutputText(BaseModel):
    category: ComplaintCategory
        
import os
from dotenv import load_dotenv
load_dotenv()

# read the environment variables
model='gpt-4o-mini'
api_key=os.getenv("OPENAI_API_KEY")

client=OpenAI(api_key=api_key)

client=instructor.patch(client)

@app.post("/predict")
def predict(input: InputText):
    payload = {"inputs": input.text}
    prompt=f"Classify the following text into different types of complaints like product, finance, shipping, customer service, etc. \n Text: {input.text}"
    response = client.chat.completions.create(
        model=model,messages=[{"role":"user","content":prompt}], 
        response_model=OutputText)
    
    return response

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
