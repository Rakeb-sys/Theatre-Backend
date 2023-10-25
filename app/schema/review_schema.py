from pydantic import BaseModel

class ReviewRequest(BaseModel):
    movie_id: str
    user_id: str
    rating: str
    comment: str | None