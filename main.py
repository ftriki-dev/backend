from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Example request model
class AddRequest(BaseModel):
    x: float
    y: float

@app.post("/add")
def add_numbers(req: AddRequest):
    # Replace this with your real factor / backtest logic
    return {"result": req.x + req.y}
