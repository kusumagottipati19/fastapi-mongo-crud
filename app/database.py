import os
import motor.motor_asyncio
from . import get_env_variable  # import utility function from __init__.py

MONGO_URI = get_env_variable("MONGO_URI")
DB_NAME = get_env_variable("DB_NAME", "my_database")  # default to 'my_database' if not set

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
database = client[DB_NAME]
todo_collection = database.get_collection("todos")
