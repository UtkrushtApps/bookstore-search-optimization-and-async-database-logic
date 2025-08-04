from fastapi import APIRouter, HTTPException, status, Depends
from typing import List
from app.schemas.schemas import BookSchema, BookCreate
from app.database import get_connection
import asyncpg

router = APIRouter()

@router.get("/books", response_model=List[BookSchema])
async def get_books():
    pool = await get_connection()
    # Inefficient: fetches all books without limit or offset
    async with pool.acquire() as conn:
        rows = await conn.fetch("SELECT id, title, author, category, published_at FROM books")
        return [BookSchema(
            id=row[0], title=row[1], author=row[2], category=row[3], published_at=row[4]
        ) for row in rows]

@router.get("/books/author/{author}", response_model=List[BookSchema])
async def get_books_by_author(author: str):
    pool = await get_connection()
    # Inefficient: sequential scan, no index on author
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT id, title, author, category, published_at FROM books WHERE author = $1", author
        )
        return [BookSchema(
            id=row[0], title=row[1], author=row[2], category=row[3], published_at=row[4]
        ) for row in rows]

@router.get("/books/category/{category}", response_model=List[BookSchema])
async def get_books_by_category(category: str):
    pool = await get_connection()
    # Inefficient: sequential scan, no index on category
    async with pool.acquire() as conn:
        rows = await conn.fetch(
            "SELECT id, title, author, category, published_at FROM books WHERE category = $1", category
        )
        return [BookSchema(
            id=row[0], title=row[1], author=row[2], category=row[3], published_at=row[4]
        ) for row in rows]

@router.post("/books", response_model=BookSchema)
async def create_book(book: BookCreate):
    pool = await get_connection()
    async with pool.acquire() as conn:
        row = await conn.fetchrow(
            "INSERT INTO books (title, author, category, published_at) VALUES ($1, $2, $3, $4) RETURNING id, title, author, category, published_at",
            book.title, book.author, book.category, book.published_at
        )
        return BookSchema(
            id=row[0], title=row[1], author=row[2], category=row[3], published_at=row[4]
        )
