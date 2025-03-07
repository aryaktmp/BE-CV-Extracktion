import pdfplumber
import io


def extract_text_from_pdf(contents: bytes) -> str:
    """Extract text from the given PDF file as bytes."""
    try:
        pdf_file = io.BytesIO(contents)
        text = ""
        with pdfplumber.open(pdf_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text if text else "No text found in PDF."
    except Exception as e:
        raise RuntimeError(f"Error processing PDF: {str(e)}")
