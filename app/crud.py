
from .database import todo_collection
from .models import TodoModel, UpdateTodoModel
from bson import ObjectId

# Convert MongoDB document into a Python dict
def todo_helper(todo) -> dict:
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo.get("description"),
        "completed": todo["completed"]
    }

async def fetch_all_todos():
    todos = []
    async for todo in todo_collection.find():
        todos.append(todo_helper(todo))
    return todos

async def fetch_one_todo(id: str):
    todo = await todo_collection.find_one({"_id": ObjectId(id)})
    return todo_helper(todo) if todo else None

async def create_todo(todo: TodoModel):
    new_todo = await todo_collection.insert_one(todo.dict())
    created_todo = await todo_collection.find_one({"_id": new_todo.inserted_id})
    return todo_helper(created_todo)

async def update_todo(id: str, data: UpdateTodoModel):
    await todo_collection.update_one(
        {"_id": ObjectId(id)},
        {"$set": {k: v for k, v in data.dict().items() if v is not None}}
    )
    updated = await todo_collection.find_one({"_id": ObjectId(id)})
    return todo_helper(updated) if updated else None

async def delete_todo(id: str):
    result = await todo_collection.delete_one({"_id": ObjectId(id)})
    return result.deleted_count > 0
