from typing import Optional , List
from webbrowser import get
from fastapi import Body, FastAPI, Response, status, HTTPException, Depends
from pydantic import BaseModel
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from sqlalchemy.orm import Session
from . import models ,schemas ,utils
from .database import engine, get_db
from sqlalchemy.exc import IntegrityError
from .routers import post , user , auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()




while True:
    try:
        conn = psycopg2.connect(host='localhost' , database='fastapi', user='postgres', password='manjulpython22', cursor_factory = RealDictCursor)
        cur = conn.cursor()
        print("Database connection was Successful")
        break
    except Exception as error:
        print("Connection Failed")
        print("Error was" , error)
        time.sleep(2)


def find_post(id):
    for p in my_posts():
        if p['id'] == id:
            return p


def find_index_post(id):
    for i , p in enumerate(my_posts):
        if p['id']== id:
            return i



app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}








