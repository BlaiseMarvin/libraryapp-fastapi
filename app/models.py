from sqlalchemy import Column, ForeignKey,Integer,String,Numeric,DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from .database import Base


class Book(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    rating=Column(Numeric(3,2),nullable=False)
    time_created=Column(DateTime(timezone=True),server_default=func.now())
    time_updated=Column(DateTime(timezone=True),onupdate=func.now())
    author_id=Column(Integer,ForeignKey("authors.id",ondelete="CASCADE"))
    author=relationship("Author")

class Author(Base):
    __tablename__="authors"
    id=Column(Integer,nullable=False,primary_key=True)
    name=Column(String,nullable=False)
    age=Column(Integer)
    time_created=Column(DateTime(timezone=True),server_default=func.now())
    time_updated=Column(DateTime(timezone=True),onupdate=func.now())


    

