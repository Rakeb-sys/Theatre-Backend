import shutil
import uuid

from fastapi import Form, UploadFile, File, HTTPException

from app.database import movie_collection
from app.schema import movie_schema


async def add_movie(
        title: str = Form(),
        year: str = Form(),
        runtime: str = Form(),
        genre: str = Form(),
        director: str = Form(),
        writer: str = Form(),
        movie_actors: list[str] = Form(...),
        plot: str = Form(),
        language: str = Form(),
        movie_Posters: list[UploadFile] = File (...),
        type: str =Form(),
):


    if not title:
        raise HTTPException(status_code=400, detail="No title")
    if not year:
        raise HTTPException(status_code=400, detail="No year")
    if not runtime:
        raise HTTPException(status_code=400, detail="No rintime")
    if not genre:
        raise HTTPException(status_code=400, detail="No genre")
    if not director:
        raise HTTPException(status_code=400, detail="No diretctor")
    if not writer:
        raise HTTPException(status_code=400, detail="No writer")
    if not movie_actors:
        raise HTTPException(status_code=400, detail="No actors")
    if not plot:
        raise HTTPException(status_code=400, detail="No plot")
    if not language:
        raise HTTPException(status_code=400, detail="No language")
    if not movie_Posters:
        raise HTTPException(status_code=400, detail="No poster")
    if not type:
        raise HTTPException(status_code=400, detail="No type")

    actors = []

    for actor in movie_actors:
        actors.append(actor)

    posters = []

    for poster in movie_Posters:
        poster_url = "public/" + uuid.uuid1().__str__() + "." + poster.filename.split(".")[1]

        with open(poster_url, "wb") as buffer:
            shutil.copyfileobj(poster.file, buffer)
        poster_url = "http://localhost:8000/" + poster_url
        posters.append(poster_url)

    movie = movie_schema (title = title, year = year, runtime =runtime, genre = genre, director = director, writer = writer, actors = actors, plot = plot, language = language, movie_Posters = posters, type = type)

    result = movie_collection.insert_one(movie.__dict__)
    _id = result.insertid
    return {"movieId": str(_id), "status": "success"}

# async def search_Movie(
#         title: str,
#
#
# ):

