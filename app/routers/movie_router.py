from dotenv import load_dotenv
from fastapi import APIRouter, Form, UploadFile, File

from app.services import movie_service

router = APIRouter()
# load_dotenv()

@router.post("/api/v1/movie")
async def addMovie(
        title: str = Form(),
        year: str = Form(),
        runtime: str = Form(),
        genre: str = Form(),
        director: str = Form(),
        writer: str = Form(),
        actors: list[str] = Form(...),
        plot: str = Form(),
        language: str = Form(),
        movie_Posters: list[UploadFile] = File (...),
        type: str =Form(),
):
    return await movie_service.add_movie(title, year, runtime, genre, director,writer, actors, plot,language,movie_Posters, type)