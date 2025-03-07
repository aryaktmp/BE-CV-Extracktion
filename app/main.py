from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import pdf_converter

app = FastAPI(
    title="PDF to Text API",
    description="API untuk mengonversi PDF menjadi teks menggunakan FastAPI dan pdfplumber",
    version="1.0.0",
)

origins = [
    "http://localhost:53346",
    "http://127.0.0.1:53346",
    "http://localhost:4200",
    "http://127.0.0.1:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdf_converter.router)


@app.get("/")
async def root():
    return {"message": "Welcome to the PDF to Text API"}
