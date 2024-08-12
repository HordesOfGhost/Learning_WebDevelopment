from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.model_dump()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_wit_tax": price_with_tax})
    return item_dict

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     item.name = item.name.capitalize()
#     item.description = item.description.title()
#     return {"item_id": item_id, **item.model_dump()}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q :Union[str, None]=None):

    item.name = item.name.capitalize()
    item.description = item.description.title()
    result = {"item_id": item_id, **item.model_dump()}
    if q:
        result.update({"q":q})
    return result