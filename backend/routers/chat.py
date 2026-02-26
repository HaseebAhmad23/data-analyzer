from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# session_id -> RAG chain, populated after upload
sessions: dict = {}


class ChatMessage(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    response: str


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatMessage):
    if payload.session_id not in sessions:
        raise HTTPException(status_code=404, detail="Session not found. Please upload a document first.")

    # TODO: run payload.message through sessions[payload.session_id] and return the answer
    chain = sessions[payload.session_id]
    result = chain.run(payload.message)

    return ChatResponse(response=result)
