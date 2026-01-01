from pydantic import BaseModel, Field
from typing import List, Dict

class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's message to the philosopher", min_length=1)

class ChatResponse(BaseModel):
    reply: str = Field(..., description="The philosopher's response to the user's message")
    analysis: List[str] = Field(..., description="The analysis of the user's message")
    status: str = "success"