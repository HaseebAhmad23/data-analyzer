import uuid

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel, HttpUrl

router = APIRouter()


class UrlInput(BaseModel):
    url: HttpUrl


class UploadResponse(BaseModel):
    session_id: str
    message: str
    source_type: str


@router.post("/upload/pdf", response_model=UploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename or not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")

    # TODO: read file bytes, run through pdf_loader, build vector store, store by session_id
    # contents = await file.read()
    session_id = str(uuid.uuid4())

    return UploadResponse(
        session_id=session_id,
        message="PDF received",
        source_type="pdf",
    )


@router.post("/upload/url", response_model=UploadResponse)
async def submit_url(payload: UrlInput):
    # TODO: fetch page with web_loader, build vector store, store by session_id
    session_id = str(uuid.uuid4())

    return UploadResponse(
        session_id=session_id,
        message="URL received",
        source_type="url",
    )
