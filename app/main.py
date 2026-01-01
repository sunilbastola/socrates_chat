from fastapi import FastAPI, HTTPException
from app.services.socrates import generate_response
from app.schemas.chat import ChatRequest, ChatResponse
from app.processor import process_text

app = FastAPI(title="Project Socrates")

@app.post("/chat")
async def chat(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        nlp_results = process_text(request.message)
        socratic_reply = generate_response(request.message)

        return ChatResponse(
            reply=socratic_reply,
            analysis=nlp_results.get("lemmas", []),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Service Error: {str(e)}")

