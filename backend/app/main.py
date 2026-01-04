from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from app.services.socrates import generate_response
from app.schemas.chat import ChatRequest, ChatResponse
from app.processor import process_text

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Project Socrates")

# Add CORS middleware to allow frontend requests
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    """Redirect to API documentation"""
    return RedirectResponse(url="/docs")

@app.post("/chat")
@app.post("/api/chat")  # Also support /api/chat for frontend
async def chat(request: ChatRequest):
    if not request.message:
        raise HTTPException(status_code=400, detail="Message cannot be empty")

    try:
        nlp_results = process_text(request.message)
        socratic_reply = generate_response(request.message)

        # Return response matching frontend expectations
        return {
            "status": "success",
            "socrates_response": socratic_reply,
            "reply": socratic_reply,  # Also include for compatibility
            "analysis": nlp_results.get("lemmas", []),
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Service Error: {str(e)}")

