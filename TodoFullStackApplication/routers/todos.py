import sys
from starlette.requests import Request
from typing import Optional
from fastapi import Depends, HTTPException, APIRouter
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user, get_user_exception
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix="/todos",
    tags=["todos"],
    responses={404: {"description": "Not found"}}
)

models.Base.metadata.create_all(bind=engine)

# Specifying the place where the Jinja2 templates live
templates = Jinja2Templates(directory="templates")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get("/", response_class=HTMLResponse)
async def readAllByUser(request: Request):
    return templates.TemplateResponse("homepage.html", {"request": request})


# In the below function called 'editTodo', the 'todo_id' field is a path parameter.
@router.get('/editTodo/{todo_id}', response_class=HTMLResponse)
async def editTodo(request: Request):
    return templates.TemplateResponse("editTodo.html", {"request": request})


@router.get('/addTodo', response_class=HTMLResponse)
async def addNewTodo(request: Request):
    return templates.TemplateResponse("addTodo.html", {"request": request})
