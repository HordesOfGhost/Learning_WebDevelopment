from typing import Set, Union
from enum import Enum

from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()


# @app.post("/items/", response_model=Item, tags=["items"])
# async def create_item(item: Item):
#     return item


# @app.get("/items/", tags=["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 42}]


# @app.get("/users/", tags=["users"])
# async def read_users():
#     return [{"username": "johndoe"}]


# class Tags(Enum):
#     items = "items"
#     users = "users"


# @app.get("/items/", tags=[Tags.items])
# async def get_items():
#     return ["Portal gun", "Plumbus"]


# @app.get("/users/", tags=[Tags.users])
# async def read_users():
#     return ["Rick", "Morty"]

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()


# @app.post(
#     "/items/",
#     response_model=Item,
#     summary="Create an item",
#     response_description= "The created item."
# )
# async def create_item(item: Item):
#     """
#         Create an item with all the information:

#         - **name**: each item must have a name
#         - **description**: a long description
#         - **price**: required
#         - **tax**: if the item doesn't have tax, you can omit this
#         - **tags**: a set of unique tag strings for this item
#     """
#     return item

# Depricate a path


@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name": "Foo", "price": 42}]


@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "johndoe"}]


@app.get("/elements/", tags=["items"], deprecated=True)
async def read_elements():
    return [{"item_id": "Foo"}]