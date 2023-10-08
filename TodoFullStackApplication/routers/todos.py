import sys
from starlette.requests import Request
from typing import Optional
from fastapi import Depends, HTTPException, APIRouter, Form
from starlette.responses import RedirectResponse
from starlette import status
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
async def readAllByUser(request: Request, database: Session = Depends(get_db)):
    # The below query will get all todos which belong to the owner with id 1.
    todos = database.query(models.Todos).filter(models.Todos.owner_id == 1).all()
    return templates.TemplateResponse("homepage.html", {"request": request, "todos": todos})


# In the below function called 'editTodo', the 'todo_id' field is a path parameter.
@router.get('/editTodo/{todo_id}', response_class=HTMLResponse)
async def editTodo(request: Request, todo_id: int, database: Session = Depends(get_db)):
    todo = database.query(models.Todos).filter(models.Todos.id == todo_id).first()
    return templates.TemplateResponse("editTodo.html", {"request": request, "todo": todo})


@router.post('/editTodo/{todo_id}', response_class=HTMLResponse)
async def saveEditedTodo(request: Request, todo_id: int, title: str = Form(...),
                         description: str = Form(...), priority: int = Form(...),
                         database: Session = Depends(get_db)):
    # grabbing the todo with id equal to the one passed as a path parameter here
    todo_model = database.query(models.Todos).filter(models.Todos.id == todo_id).first()

    # updating the title of todo
    todo_model.title = title

    # updating the description of todo
    todo_model.description = description

    # updating the priority of todo
    todo_model.priority = priority

    # adding the updated todo to the database
    database.add(todo_model)

    # finalizing the database commit
    database.commit()
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get("/deleteTodo/{todo_id}")
async def deleteTodo(request: Request, todo_id: int,
                     database: Session = Depends(get_db)):
    todo_model = database.query(models.Todos).filter(models.Todos.id == todo_id) \
        .filter(models.Todos.owner_id == 1).first()
    if todo_model is None:
        return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)

    database.query(models.Todos).filter(models.Todos.id == todo_id).delete()

    database.commit()
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.post('/addTodo', response_class=HTMLResponse)
async def createTodo(request: Request, title: str = Form(...), description: str = Form(...),
                     priority: int = Form(...), database: Session = Depends(get_db)):
    # Create an instance of the Todos model
    todo_model = models.Todos(
        title=title,
        description=description,
        priority=priority,
        complete=False,
        owner_id=1
    )

    database.add(todo_model)
    database.commit()
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)


@router.get('/addTodo', response_class=HTMLResponse)
async def addNewTodo(request: Request):
    return templates.TemplateResponse("addTodo.html", {"request": request})


@router.get("/completeTodo/{todo_id}", response_class=HTMLResponse)
async def completeTodo(request: Request, todo_id: int, database: Session = Depends(get_db)):
    todo_model = database.query(models.Todos).filter(models.Todos.id == todo_id).first()
    todo_model.complete = not todo_model.complete

    database.add(todo_model)
    database.commit()

    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)
