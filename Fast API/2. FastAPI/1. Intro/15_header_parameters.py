from typing import Union, List

from fastapi import FastAPI, Header
from typing_extensions import Annotated

app = FastAPI()

# @app.get("/items/")
# async def read_items(
#     strange_header: Annotated[
#         Union[str, None], Header(convert_underscores=False)
#     ] = None,
# ):
#     return {"strange_header": strange_header}

@app.get("/items/")
async def read_items(x_token: Annotated[Union[List[str], None], Header()] = None):
    return {"User-Agent": x_token}