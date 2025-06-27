from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import models, database

cache = {}

router = APIRouter(
    prefix="/books",
    tags=["books"]
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def get_books(db: Session = Depends(get_db)):
    cache.clear()  # ⬅️ Add this line temporarily

    if "books" in cache:
        print("📦 Returning books from cache")
        return cache["books"]
    
    books = db.query(models.Book).all()
    cache["books"] = books
    print("💾 Cached the books from DB")
    return books


@router.post("/")
def add_book(book: dict, db: Session = Depends(get_db)):
    new_book = models.Book(title=book["title"], author=book["author"])
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book
@router.get("/{book_id}/reviews")
def get_reviews(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book.reviews

@router.post("/{book_id}/reviews")
def add_review(book_id: int, review: dict, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    new_review = models.Review(text=review["text"], book_id=book.id)
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    return new_review
