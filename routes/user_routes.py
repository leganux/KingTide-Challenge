import datetime
import traceback

from fastapi import APIRouter, HTTPException
from models.user_model import User
from schemas.user_schema import users_serializer
from bson import ObjectId
from config.db import collection

user = APIRouter(
    prefix="/api/v1/user",
    tags=["user"],
    responses={
        404: {"description": "Not found", "example": {"error": "error"}},
        200: {"description": "OK"},
        500: {"description": "Internal server error"},
    }
)


@user.post("/")
async def create_one(user: User):
    try:
        user.created_at = datetime.datetime.utcnow()
        _id = collection.insert_one(dict(user))
        user = users_serializer(collection.find({"_id": _id.inserted_id}))
        return {
            "status": "Ok",
            "data": user,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@user.get("/")
async def get_all():
    try:
        users = users_serializer(collection.find())
        return {
            "status": "Ok",
            "data": users,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@user.get("/{id}")
async def get_one(id: str):
    try:
        user = users_serializer(collection.find({"_id": ObjectId(id)}))
        if user is None or len(user) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "status": "Ok",
            "data": user,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@user.put("/{id}")
async def update(id: str, user: User):
    try:
        collection.find_one_and_update(
            {
                "_id": ObjectId(id)
            },
            {
                "$set": dict(user)
            })

        user = users_serializer(collection.find({"_id": ObjectId(id)}))
        if user is None or len(user) == 0:
            raise HTTPException(status_code=404, detail="User not found")

        return {
            "status": "Ok",
            "data": user,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")


@user.delete("/{id}")
async def update(id: str):
    try:
        collection.find_one_and_delete({"_id": ObjectId(id)})
        users = users_serializer(collection.find())

        return {
            "status": "Ok",
            "data": users,
            "success": True
        }
    except HTTPException as e:
        raise e  # Re-raise the HTTPException to return the appropriate response
    except Exception as e:
        traceback_str = traceback.format_exc()
        print("ERROR", e)
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {traceback_str}")
