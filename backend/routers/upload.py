import uuid
import tempfile, os

from fastapi import APIRouter, File, HTTPException, UploadFile
from pydantic import BaseModel, HttpUrl
from backend.session_store import session_store
from backend.services.pdf_loader import load_pdf
from backend.services.web_loader import load_url
from backend.services.rag_chain import create_rag_chain

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

    contents = await file.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    documents = load_pdf(tmp_path)
    os.unlink(tmp_path)
    if not documents:
        raise HTTPException(status_code=422, detail="No text could be extracted from this PDF. It may be a scanned or image-based PDF.")
    qa_chain = create_rag_chain(documents)
    session_id = str(uuid.uuid4())
    session_store[session_id] = qa_chain

    return UploadResponse(
        session_id=session_id,
        message="PDF received",
        source_type="pdf",
    )


@router.post("/upload/url", response_model=UploadResponse)
async def submit_url(payload: UrlInput):
    documents = load_url(str(payload.url))
    qa_chain = create_rag_chain(documents)
    session_id = str(uuid.uuid4())
    session_store[session_id] = qa_chain

    return UploadResponse(
        session_id=session_id,
        message="URL received",
        source_type="url",
    )
