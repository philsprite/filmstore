from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.v1.endpoints.movie import crud, schemas
from app.core.database import SessionLocal

router = APIRouter(tags=["movies"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.MovieRead, status_code=status.HTTP_201_CREATED)
def create_movie(movie_in: schemas.MovieCreate, db: Session = Depends(get_db)):
    return crud.create_movie(db, movie_in)

@router.get("/", response_model=list[schemas.MovieRead])
def list_movies(db: Session = Depends(get_db)):
    return crud.list_movies(db)

@router.get("/{movie_id}", response_model=schemas.MovieRead)
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Movie not found")
    return movie

@router.put("/{movie_id}", response_model=schemas.MovieRead)
def update_movie(movie_id: int, movie_in: schemas.MovieCreate, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Movie not found")
    return crud.update_movie(db, movie_id, movie_in)

@router.delete("/{movie_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = crud.get_movie(db, movie_id)
    if not movie:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "Movie not found")
    crud.delete_movie(db, movie_id)
