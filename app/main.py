from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from app.routers import user_router, review_router, report_router
import app.routers.movie_router as movie_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}




app.include_router(movie_router.router, tags=["Movie"])
app.include_router(user_router.router, tags=["user"])
app.include_router(review_router.router, tags=["review"])

app.mount("/public", StaticFiles(directory="public"), name="static")
