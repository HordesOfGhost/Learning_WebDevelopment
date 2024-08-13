from typing import Union, List
from fastapi import FastAPI

from fastapi import FastAPI, Query
from typing_extensions import Annotated

app = FastAPI()

# Optional

# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None] , Query(min_length=3, max_length=10)] = 'rick'):
#     results = {"items": [ {"item_id":"Foo"}, {"item_id":"Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results


# Required

# @app.get("/items/")
# async def read_items(q: Annotated[str, Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Required with None

# @app.get("/items/")
# async def read_items(q: Annotated[Union[str, None], Query(min_length=3)] = ...):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Multiple Values

# @app.get("/items/")
# async def read_items(q: Annotated[Union[List[str], None], Query()] = None):
#     results = {"items": [{"item_id":"Foo"}]}
#     if q:
#         results.update({'q':q})
#     return results


# @app.get("/items/")
# async def read_items(q: Annotated[Union[list, None], Query()] = None):
#     results = {"items": [{"item_id":"Foo"}]}
#     if q:
#         results.update({'q':q})
#     return results

# Metadata

# @app.get("/items/")
# async def read_items(
#     q: Annotated[Union[str, None], Query(title="Query string", 
#                                          description = "Description of api", 
#                                          alias = "item-query",
#                                          min_length=3,
#                                          depricated=True)] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

# Remove hidden query

@app.get("/items/")
async def read_items(
    hidden_query: Annotated[Union[str, None], Query(include_in_schema=True)] = None,
):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}
