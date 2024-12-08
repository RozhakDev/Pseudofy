from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import pseudocode
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Pseudofy API",
    description="API untuk menghasilkan pseudocode dari deskripsi masalah menggunakan AI.",
    version="2.0.0"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

app.include_router(pseudocode.router, prefix="/api/v1/pseudocode", tags=["Pseudocode"])

@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint root untuk verifikasi bahwa API berjalan.
    """
    return {"message": "Welcome to Pseudofy API. Visit /docs for documentation."}