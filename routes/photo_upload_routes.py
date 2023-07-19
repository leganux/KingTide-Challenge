import os
import traceback

from fastapi import FastAPI, File, UploadFile, HTTPException, APIRouter

max_file_size = 5 * 1024 * 1024

upload = APIRouter(
    prefix="/api/v1/photo",
    tags=["upload_photo"],
    responses={
        404: {"description": "Not found", "example": {"error": "error"}},
        200: {"description": "OK"},
        500: {"description": "Internal server error"},
    }
)


@upload.post("/")
async def upload_photo(uploaded_file: UploadFile = File(...)):
    try:

        file_size = 0
        with open(uploaded_file.filename, "wb") as file_object:
            for chunk in uploaded_file.file:
                file_size += len(chunk)
                if file_size > max_file_size:
                    raise HTTPException(status_code=400, detail="El archivo excede el tamaño máximo permitido")



        file_extension = os.path.splitext(uploaded_file.filename)[1]
        allowed_extensions = ['.png', '.jpeg', '.jpg']
        if file_extension.lower() not in allowed_extensions:
            raise HTTPException(status_code=400, detail="El archivo debe ser de tipo PNG, JPEG, o JPG")

        directory = "files/photo/"
        os.makedirs(directory, exist_ok=True)
        file_location = f"files/photo/{uploaded_file.filename}"
        with open(file_location, "wb+") as file_object:
            file_object.write(uploaded_file.file.read())

        return {
            "status": "Ok",
            "data": {
                "name": uploaded_file.filename,
                "location": file_location,
            },
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")
