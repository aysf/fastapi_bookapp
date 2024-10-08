from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int 
    title: str 
    author: str 
    description: str 
    rating: int

    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1, lt=6)

BOOK = [
    Book(1, 'Computer Science Pro', 'Codingwithroby', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'Codingwithroby', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'Codingwithroby', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'Coding with Harry', 'Author 2', 'Book Description', 1),
]

@app.get("/books")
async def read_all_books():
    return BOOK

@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    print(type(new_book))
    BOOK.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOK) == 0 else BOOK[-1].id + 1
    return book