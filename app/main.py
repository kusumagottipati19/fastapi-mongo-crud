
from fastapi import FastAPI, HTTPException
from .models import TodoModel, UpdateTodoModel
from . import crud

app = FastAPI()

@app.get("/todos")
async def get_todos():
    return await crud.fetch_all_todos()

@app.get("/todos/{id}")
async def get_todo(id: str):
    todo = await crud.fetch_one_todo(id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@app.post("/todos")
async def create_todo(todo: TodoModel):
    return await crud.create_todo(todo)

@app.put("/todos/{id}")
async def update_todo(id: str, todo: UpdateTodoModel):
    updated = await crud.update_todo(id, todo)
    if not updated:
        raise HTTPException(status_code=404, detail="Todo not found")
    return updated

@app.delete("/todos/{id}")
async def delete_todo(id: str):
    deleted = await crud.delete_todo(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
