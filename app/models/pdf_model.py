from pydantic import BaseModel


class PDFTextResponse(BaseModel):
    text: str
    file_name: str
    file_base64: str
