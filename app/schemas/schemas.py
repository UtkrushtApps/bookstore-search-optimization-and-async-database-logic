from pydantic import BaseModel
from typing import Optional
from datetime import date

class BookSchema(BaseModel):
    id: int
    title: str
    author: str
    category: str
    published_at: Optional[date]

    class Config:
        orm_mode = True

class BookCreate(BaseModel):
    title: str
    author: str
    category: str
    published_at: Optional[date]
