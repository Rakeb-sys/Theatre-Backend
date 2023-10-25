from bson import ObjectId
from fastapi import HTTPException

from app.database import movie_collection, user_collection, review_collection
from app.schema.review_schema import ReviewRequest


async def movie_review(review: ReviewRequest):
    if not review.user_id:
        raise HTTPException(status_code=400, detail="no user name")
    if not review.movie_id:
        raise HTTPException(status_code=400, detail="no movie selected")
    if not review.rating:
        raise HTTPException(status_code=400, detail="no rating")

    movie = movie_collection.find_one({"_id": ObjectId(review.movie_id)})

    if movie is None:
        raise HTTPException(status_code=404, detail="movie not found")

    user = user_collection.find_one({"_id": ObjectId(review.user_id)})

    if user is None:
        raise HTTPException(status_code=404, detail="no such user found")

    if review.rating:
        for rate in review.rating:
            if rate not in range(10) and rate <= 0:
                raise HTTPException(status_code=200, detail="rating should between 1 - 10")

    result = review_collection.inser_one(review.__dict__)
    _id = result.inserted_id
    return {"status": "success", "reviewId": str(_id)}