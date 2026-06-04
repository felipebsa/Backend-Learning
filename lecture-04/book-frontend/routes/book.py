from fastapi import APIRouter, HTTPException
from database import session_base
from schemas.book import BookSchema
from models.book import Book

router = APIRouter()

@router.get("/")
def home():
    return {"message": "successful"}

@router.post("/books")
def book_create(book: BookSchema):
    db = session_base()
    db_book = Book(
        title = book.title,
        author = book.author,
        read = book.read
    )
    db.add(db_book)
    db.commit()
    db.close()
    return {"message": "book add successful "}

@router.get("/books/{id}")
def books_id(id: int):
    db = session_base()
    book = db.query(Book).filter_by(id=id).first()
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    return book


@router.get("/books")
def end_books(read: bool = None):
    db = session_base()
    if read is None:
        return db.query(Book).all()
    return db.query(Book).filter_by(read=read).all()

@router.delete("/books/{id}")
def book_remove(id: int):
    db = session_base()
    book = db.query(Book).filter_by(id=id).first()
    if not book:
        raise HTTPException(status_code=404, detail="book not found")
    db.delete(book)
    db.commit()
    db.close()
    return {"message": "delete book successful"}

@router.put("/books/{id}")
def put_book(id: int, book: BookSchema):
    db = session_base()
    db_book = db.query(Book).filter_by(id=id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="book not found")
    db_book.title = book.title
    db_book.author = book.author
    db_book.read = book.read 
    db.commit()
    db.close()
    return {"message": "put successful"}