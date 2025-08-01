# routes.py

from fastapi import APIRouter, UploadFile, File
from utils import load_and_split_pdf

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    contents = await file.read()
    file_path = f"/tmp/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)
    
    split_docs = load_and_split_pdf(file_path)
    return {"chunks": [doc.page_content for doc in split_docs[:5]]}  # Just returning top 5 chunks for now
