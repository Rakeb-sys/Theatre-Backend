from fastapi import APIRouter

from app.database import review_collection
from app.routers.movie_router import router
from app.schema.review_schema import ReviewRequest
from app.services import review_service

router = APIRouter()
@router.post("/api/v1/review")
async def movieReview(review: ReviewRequest):
    return await(review_service.movie_review(review))