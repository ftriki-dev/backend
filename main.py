from fastapi import FastAPI
from pydantic import BaseModel
from vertexai.generative_models import GenerativeModel
import vertexai

app = FastAPI()

# Example request model
class AddRequest(BaseModel):
    x: float
    y: float

@app.post("/add")
def add_numbers(req: AddRequest):
    # Replace this with your real factor / backtest logic
    return {"result": req.x + req.y}



vertexai.init(project="ancient-torch-480602-a1", location="us-central1")


class LLMRequest(BaseModel):
    prompt: str

@app.post("/ask_llm")
def ask_llm(req: LLMRequest):
    model = GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(req.prompt)
    return {"output": response.text}

