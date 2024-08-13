from typing import Union

from fastapi import FastAPI, Path,Body
from pydantic import BaseModel

from typing import List
from typing_extensions import Annotated

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None]=None

# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
#     user: Union[User, None] = None,
#     importance: Annotated[Union[List[str],None], Body()] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q":q})
#     if item:
#         results.update({"item": item})
#     if user:
#         results.update({'user':user})
#     if importance:
#         results.update({'importance':importance})
#     return results

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    results = {"item_id": item_id, "item": item}
    return results
