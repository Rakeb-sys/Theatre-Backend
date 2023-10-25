from bson import ObjectId
from fastapi import HTTPException

from app.database import user_collection
from app.schema.user_schema import UserRequest


async def users(user: UserRequest):
    if not user.username:
        raise HTTPException(status_code=200, detail="no user name")
    if not user.email:
        raise HTTPException(status_code=200, detail="no email")

    us = user_collection.find_one({"username": ObjectId(user.username)})
    if us is not None:
        raise HTTPException(status_code=400, detail="username already exist")
    user_movie = user_collection.insert_one(user.__dict__)
    _id = user_movie.insertedid

    return {"status":"success", "userId": str(_id)}

