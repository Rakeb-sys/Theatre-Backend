from fastapi import APIRouter

from app.routers.movie_router import router
from app.schema.user_schema import UserRequest
from app.services import user_service

router = APIRouter()
@router.post("/api/v1/user")
async def addUser(user: UserRequest):
    return await user_service.users(user)