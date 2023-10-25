import datetime

from pydantic import BaseModel

class MovieSchema(BaseModel):
    title: str
    year: str
    runtime: str
    genre: str
    director: str
    writer: str
    actors: list
    plot: str
    language: str
    poster: list
    type: str

