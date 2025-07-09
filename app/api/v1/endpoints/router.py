from fastapi import APIRouter

from app.api.v1.endpoints.movie.router import router as movie_router

# … importiere hier alle Resource-Router

router = APIRouter(prefix="/api/v1")

router.include_router(movie_router, prefix="/movies")

# … jeweils mit passendem Prefix
