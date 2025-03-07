# PDF to Text API

## Description
This API is developed using **FastAPI** to convert **PDF files** into **text** and return the results in **Base64 format**. It also allows users to download the extracted text as a `.txt` file.

## Project Structure

```
app/
│── models/
│   ├── pdf_model.py         # Pydantic model for API response
│
│── routes/
│   ├── pdf_converter.py     # Router for handling PDF to text conversion
│
│── services/
│   ├── pdf_service.py       # Service for processing PDFs
|
│── config.py            # Application configuration
│── main.py              # Entry point for the FastAPI application
│
├── .gitignore
├── README.md
├── requirements.txt         # List of dependencies
├── run.py                   # Script to start the server
```

## Installation and Running the Server
Ensure you have **Python 3.8+** installed, then follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/aryaktmp/BE-CV-Extracktion.git BE-CV-Extracktion
cd BE-CV-Extracktion
```

```
pip install -r requirements.txt
```

### 3. Start the FastAPI Server
```bash
py run.py
```
The server will be running at `http://127.0.0.1:8000`.
