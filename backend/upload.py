from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import os
from auth import get_current_user
import requests

router = APIRouter()

N8N_WEBHOOK_URL = "http://n8n:5678/webhook/resume-upload"

@router.post("/upload")
async def upload_resume(
    file: UploadFile = File(...),
    current_user: dict = Depends(get_current_user)
):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    try:
        # Save file temporarily
        file_location = f"/tmp/{file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(file.file.read())

        # Prepare payload for n8n
        payload = {
            "filename": file.filename,
            "filepath": file_location,
            "user": current_user["username"]
        }

        # Send to n8n webhook
        response = requests.post(N8N_WEBHOOK_URL, json=payload)

        if response.status_code != 200:
            raise HTTPException(status_code=500, detail="Error processing resume")

        return JSONResponse(
            status_code=200,
            content={"message": "Resume uploaded and processing started"}
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))