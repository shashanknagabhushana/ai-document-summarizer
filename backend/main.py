from pathlib import Path

from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from backend.summarizer import summarize_text
from backend.utils import extract_text


# --------------------------------------------------
# Application
# --------------------------------------------------

app = FastAPI(
    title="AI Document Summarizer",
    description="A document summarization system",
    version="1.0.0"
)


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

UPLOAD_DIR = BASE_DIR / "uploads"
FRONTEND_DIR = BASE_DIR / "frontend"

UPLOAD_DIR.mkdir(exist_ok=True)


# --------------------------------------------------
# Supported file types
# --------------------------------------------------

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}


# --------------------------------------------------
# Serve frontend files
# --------------------------------------------------

app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR),
    name="static"
)


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.get("/")
def home():
    return FileResponse(
        FRONTEND_DIR / "index.html"
    )


# --------------------------------------------------
# Health check
# --------------------------------------------------

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# --------------------------------------------------
# Upload document
# --------------------------------------------------

@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    # Check filename
    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    # Get file extension
    extension = Path(file.filename).suffix.lower()

    # Check file type
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only PDF, DOCX, and TXT files are supported."
        )

    # Prevent unsafe paths
    filename = Path(file.filename).name

    file_path = UPLOAD_DIR / filename

    # Read file
    content = await file.read()

    # Save file
    file_path.write_bytes(content)

    # Extract text
    try:

        text = extract_text(
            str(file_path)
        )

    except Exception as error:

        file_path.unlink(
            missing_ok=True
        )

        raise HTTPException(
            status_code=500,
            detail=f"Could not extract text: {str(error)}"
        )

    # Check extracted text
    if not text.strip():

        file_path.unlink(
            missing_ok=True
        )

        raise HTTPException(
            status_code=400,
            detail="The uploaded document contains no readable text."
        )

    # Generate summary
    try:

        summary = summarize_text(text)

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=f"Could not generate summary: {str(error)}"
        )

    # Return result
    return {
        "filename": filename,
        "characters": len(text),
        "summary": summary
    }
