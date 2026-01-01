from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.services.socrates import get_socratic_response

app = FastAPI(title="Project Socrates")

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    try:
        response = get_socratic_response(request.message)
        return {"reply": response}
    except Exception as e:
        # Professional logging (simplifed for now)
        raise HTTPException(status_code=500, detail=f"AI Service Error: {str(e)}")