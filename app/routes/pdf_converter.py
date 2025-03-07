import base64
import os
from fastapi import APIRouter, File, UploadFile
from app.models.pdf_model import PDFTextResponse
from app.services.pdf_service import extract_text_from_pdf
from fastapi import HTTPException

router = APIRouter()


@router.post("/api/convert-pdf-to-text")
async def convert_pdf_to_text(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400, detail="Invalid file format. Only PDFs are allowed."
        )

    try:
        pdf_contents = await file.read()

        text = extract_text_from_pdf(pdf_contents)

        base64_text = convert_text_to_base64(text)

        file_name = os.path.splitext(file.filename)[0] or "converted-text" + ".txt"

        return PDFTextResponse(
            text=text,
            file_name=file_name,
            file_base64=base64_text,
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")


def convert_text_to_base64(text: str) -> str:
    """Convert Text to Base64"""
    try:
        encoded_text = base64.b64encode(text.encode("utf-8")).decode("utf-8")
        return encoded_text
    except Exception as e:
        raise RuntimeError(f"Error converting text to Base64: {str(e)}")
