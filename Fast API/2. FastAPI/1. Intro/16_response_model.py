from typing import List, Union, Any

from fastapi import FastAPI, Response
from pydantic import BaseModel, EmailStr
from fastapi.responses import JSONResponse, RedirectResponse

app = FastAPI()

# Set return type in function

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []


# @app.post("/items/")
# async def create_item(item: Item) -> Item:
#     return item


# @app.get("/items/")
# async def read_items() -> List[Item]:
#     return [
#         Item(name="Portal Gun", price=42.0),
#         Item(name="Plumbus", price=32.0),
#     ]


# Set return type in decorators

# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = []


# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item


# @app.get("/items/", response_model=List[Item])
# async def read_items() -> Any:
#     return [
#         {"name": "Portal Gun", "price": 42.0},
#         {"name": "Plumbus", "price": 32.0},
#     ]

# Return the same output data

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# # Don't do this in production!
# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user

# Add an output model in response_model

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user

# Return by Inherting the class

# class BaseUser(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Union[str, None] = None


# class UserIn(BaseUser):
#     password: str


# @app.post("/user/")
# async def create_user(user: UserIn) -> BaseUser:
#     return user

# Other Return Type Annotations
# Response

# @app.get("/portal")
# async def get_portal(teleport: bool = False) -> Response:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# @app.get("/portal", response_model=None)
# async def get_portal(teleport: bool = False) -> Union[Response, dict]:
#     if teleport:
#         return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
#     return {"message": "Here's your interdimensional portal."}




class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


# @app.get("/items/{item_id}", response_model=Item, response_model_include_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: float = 10.5
    tags: List[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get("/items/{item_id}", response_model=Item, response_model_exclude=['tax','tags'])
async def read_item(item_id: str):
    return items[item_id]