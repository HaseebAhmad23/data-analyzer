from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import health, upload, chat
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Data Analyzer API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router, tags=["Health"])
app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])


@app.get("/")
async def root():
    return {"message": "Data Analyzer API", "docs": "/docs"}
