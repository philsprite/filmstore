from sqlalchemy.orm import Session
from app.database.models import Movie
from app.api.v1.endpoints.movie.schemas import MovieCreate

def create_movie(db: Session, movie_in: MovieCreate) -> Movie:
    movie = Movie(**movie_in.model_dump())
    db.add(movie)
    db.commit()
    db.refresh(movie)
    return movie

def get_movie(db: Session, movie_id: int) -> Movie | None:
    return db.get(Movie, movie_id)

def list_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()

def update_movie(db: Session, movie_id: int, movie_in: MovieCreate) -> Movie:
    movie = db.get(Movie, movie_id)
    for k, v in movie_in.model_dump().items():
        setattr(movie, k, v)
    db.commit()
    db.refresh(movie)
    return movie

def delete_movie(db: Session, movie_id: int) -> None:
    movie = db.get(Movie, movie_id)
    db.delete(movie)
    db.commit()
