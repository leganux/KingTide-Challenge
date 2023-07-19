import traceback

from fastapi import APIRouter, HTTPException
from models.files_model import File
from schemas.file_schema import file_serializer, files_serializer
from bson import ObjectId
from config.db import collection_files

file = APIRouter(
    prefix="/api/v1/file",
    tags=["files"],
    responses={
        404: {"description": "Not found", "example": {"error": "error"}},
        200: {"description": "OK"},
        500: {"description": "Internal server error"},
    }
)


@file.post("/")
async def create_one(file: File):
    try:
        _id = collection_files.insert_one(dict(file))
        file = files_serializer(collection_files.find({"_id": _id.inserted_id}))
        return {
            "status": "Ok",
            "data": file,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@file.get("/")
async def get_all():
    try:
        files = files_serializer(collection_files.find())
        return {
            "status": "Ok",
            "data": files,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@file.get("/{id}")
async def get_one(id: str):
    try:
        file = files_serializer(collection_files.find({"_id": ObjectId(id)}))
        if file is None or len(file) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "status": "Ok",
            "data": file,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@file.put("/{id}")
async def update(id: str, file: File):
    try:
        collection_files.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": dict(file)
            })

        file = files_serializer(collection_files.find({"_id": ObjectId(id)}))
        if file is None or len(file) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "status": "Ok",
            "data": file,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@file.delete("/{id}")
async def update(id: str):
    try:
        collection_files.find_one_and_delete({"_id": ObjectId(id)})
        files = files_serializer(collection_files.find())

        return {
            "status": "Ok",
            "data": files,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")
