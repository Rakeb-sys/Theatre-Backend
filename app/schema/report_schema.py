import datetime

from pydantic import BaseModel

class ReviewReport(BaseModel):
    reviewData: dict[str, int]

