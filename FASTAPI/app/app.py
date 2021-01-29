from fastapi import FastAPI

app = FastAPI()

# Default route


@app.get("/", tags=['root'])
async def root() -> dict:
    return {"Ping": "Pong"}


# Get [Read] Todo Route
@app.get("/todo", tags=['Todos'])
async def get_todos() -> dict:
    return {"Data": todos}


# Post [Create] Todo Route
@app.post("/todo", tags=["Todos"])
async def add_todo(todo: dict) -> dict:
    todos.append(todo)
    return {
        "data": "A Todo is Added!"
    }


# PUT  [Update] Todo Route
@app.put("/todo/{id}", tags=["Todos"])
async def update_todo(id: int, body: dict) -> dict:
    for todo in todos:
        if (int(todo["ID"])) == id:
            todo["Activity"] = body["Activity"]
            return {
                "data": f"Todo with id {id} has been updated"
            }
    return {
        "data": f"This Todo with id {id} is not found!"
    }


# Delete Todo Route
@app.delete("/todo/{id}", tags=["Todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["ID"]) == id:
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
        "ID": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "ID": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]
