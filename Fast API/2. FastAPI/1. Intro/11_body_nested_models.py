from typing import Union, List, Set, Dict

from fastapi import FastAPI
from pydantic import BaseModel,HttpUrl

app = FastAPI()


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: List[str] = set()


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"iteim_id": item_id, "item":item}
#     return results


# Nested Models
    
# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     # image: Union[Image, None] = None # Nested 
#     image: Union[List[Image], None] = None


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# Deeply Nested Models

# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     images: Union[List[Image], None] = None


# class Offer(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     items: List[Item]


# @app.post("/offers/{item_id}")
# async def create_offer(offer: Offer, item_id: Union[int,None] = None):
#     offer = dict(offer)
#     if item_id:
#         offer.update({'item_id':item_id})
#     return offer

# Extra

# app = FastAPI()


# class Image(BaseModel):
#     url: HttpUrl
#     name: str


# @app.post("/images/multiple/")
# async def create_multiple_images(images: List[Image]):
#     return images

# Bodies of Arbitary Dicts


@app.post("/index-weights/")
async def create_index_weights(weights: Dict[int, float]):
    return weights