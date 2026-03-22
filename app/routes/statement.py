from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from app.services.parser import parse_statement
from app.services.analyzer import analyze_transactions
from app.services.ai_service import get_ai_suggestions
import os, shutil

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_statement(file: UploadFile = File(...)):
    # Validate file type
    allowed_types = [".xlsx", ".csv", ".pdf"]
    ext = os.path.splitext(file.filename)[-1].lower()
    if ext not in allowed_types:
        raise HTTPException(status_code=400, detail=f"Unsupported file type: {ext}")

    # Save uploaded file temporarily
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        # Step 1: Parse the file
        transactions = parse_statement(file_path, ext)

        # Step 2: Analyze transactions
        analysis = analyze_transactions(transactions)

        # Step 3: Get AI suggestions
        suggestions = get_ai_suggestions(analysis)

        return JSONResponse(content={
            "transactions": transactions,
            "analysis": analysis,
            "suggestions": suggestions
        })
    finally:
        # Clean up uploaded file
        if os.path.exists(file_path):
            os.remove(file_path)
