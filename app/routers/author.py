from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas,models

router=APIRouter(
    prefix="/authors",
    tags=["Authors"]
)

@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.AuthorRet])
def get_authors(db:Session=Depends(get_db)):
    authors=db.query(models.Author).all()
    return authors

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Author)
def add_author(author:schemas.Author,db:Session=Depends(get_db)):
    new_author=models.Author(**author.dict())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author