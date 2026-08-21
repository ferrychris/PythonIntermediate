from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class ChatRequest(BaseModel):
    user_id: str
    question: str
@app.get("/")
def Home():
    return {
        "experts": [
            {"id": 1, "name": "John"},
            {"id": 2, "name": "Sarah"}
        ]
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return {"message": "Hello, I am John", "user_id": request.user_id, "question": request.question}