from fastapi import APIRouter,status,Depends
from typing import List
from sqlalchemy.orm import Session
from .. import models
from .. import schemas
from ..database import get_db

router=APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.Book])
def get_books(db:Session=Depends(get_db)):
    books=db.query(models.Book).all()
    return books

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Book)
def add_books(book:schemas.Book,db:Session=Depends(get_db)):
    new_book=models.Book(**book.dict())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

