from fastapi import FastAPI,status
from fastapi.middleware.cors import CORSMiddleware
from .routers import author,book
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins=["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(author.router)
app.include_router(book.router)

@app.get("/",status_code=status.HTTP_200_OK)
def root():
    return {"Welcome to Library app"}