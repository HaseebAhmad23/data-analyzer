from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from backend.session_store import session_store

router = APIRouter()

class ChatMessage(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatMessage):
    if payload.session_id not in session_store:
        raise HTTPException(status_code=404, detail="Session not found. Please upload a document first.")

    # TODO: run payload.message through session_store[payload.session_id] and return the answer
    chain = session_store[payload.session_id]
    result = chain.run(payload.message)

    return ChatResponse(response=result)
