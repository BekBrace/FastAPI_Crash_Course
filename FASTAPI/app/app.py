# Importing the FastApi class
from fastapi import FastAPI

# Creating an app object
app = FastAPI()

# Default route

# A minimal app to demonstrate the get request 
@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping": "Pong"}


# GET -- > Read Todo 
@app.get("/todo", tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": todos}


# Post -- > Create Todo
@app.post("/todo", tags=["Todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A Todo is Added!"
    }


# PUT  -- > Update Todo
@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if (int(todo["id"])) == id:
            todo["Activity"] = body["Activity"]
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"This Todo with id {id} is not found!"
    }


# DELETE --> Delete Todo 
@app.delete("/todo/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return{
                "data": f"Todo with id {id} has been deleted!"
            }
    return {
        "data": f"Todo with id {id} was not found!"
    }

# Todos List

todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]
