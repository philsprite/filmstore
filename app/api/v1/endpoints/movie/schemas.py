from pydantic import BaseModel

class MovieBase(BaseModel):
    title: str
    description: str | None = None
    year: int | None = None

class MovieCreate(MovieBase):
    pass

class MovieRead(MovieBase):
    id: int

    class Config:
        orm_mode = True
