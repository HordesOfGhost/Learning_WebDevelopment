from typing import Union

from fastapi import FastAPI, Path, Query
from typing_extensions import Annotated

app = FastAPI()

# Path Parameters

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id: Annotated[int, Path(title = "The ID of item to get")],
#     q: Annotated[Union[str, None], Query(alias='item-query')] =None):

#     results = {"item_id":item_id}
#     if q:
#         results.update({"q":q})
#     return results

# Number Validations

@app.get("/items/{item_id}")
async def read_items(
    item_id: Annotated[int, Path(title="The ID of the item to get", ge=1, le=11)], 
    q: str,
    size: Annotated[float, Query(ge=0.0,lt=1.5)]
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q,"size":size})
    return results
