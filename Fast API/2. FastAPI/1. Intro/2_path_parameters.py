from fastapi import FastAPI

app = FastAPI()

# Get
# @app.get("/items/{item_id}")
# async def read_item(item_id):
#     return {"item_id": item_id}

# Get specific type data
# @app.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id_int": item_id}


@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the current user"}


@app.get("/users/{user_id}")
async def read_user_me(user_id: str):
    return {"user_id" : user_id}