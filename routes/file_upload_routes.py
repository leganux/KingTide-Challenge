import os
import traceback
import shutil

max_file_size = 5 * 1024 * 1024

from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter, Request

upload = APIRouter(
    prefix="/api/v1/files",
    tags=["upload_files"],
    responses={
        404: {"description": "Not found", "example": {"error": "error"}},
        200: {"description": "OK"},
        500: {"description": "Internal server error"},
    }
)


@upload.post("/")
async def upload_file(request: Request, uploaded_file: UploadFile = File(...)):
    try:

        file_extension = os.path.splitext(uploaded_file.filename)[1]
        allowed_extensions = ['.doc', '.docx', '.pdf']
        if file_extension.lower() not in allowed_extensions:
            raise HTTPException(status_code=400, detail="El archivo debe ser de tipo PDF, DOCX, o DOC")

        directory = "files/docs"
        os.makedirs(directory, exist_ok=True)

        with open(directory + '/' + uploaded_file.filename, "wb") as buffer:
            shutil.copyfileobj(uploaded_file.file, buffer)

        host = request.headers.get("host")
        protocol = request.headers.get("x-forwarded-proto") or request.url.scheme

        return {
            "status": "Ok",
            "data": {
                "name": uploaded_file.filename,
                "location": f"{protocol}://{host}/{directory + '/' + uploaded_file.filename}",
            },
            "success": True
        }



    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")
