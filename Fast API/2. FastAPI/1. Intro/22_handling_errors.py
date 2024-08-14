from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, PlainTextResponse

from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


# items = {'foo': 'The Foo Wrestlers'}

# @app.get("/items/{item_id}")
# async def read_items(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code=404, 
#                             detail="Item not Found",
#                             headers={"X-Error": "There goes my error."},
#                             )
#     return {"item": items[item_id]}


# Add Custom Handlers

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name

# app = FastAPI()

# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code = 418,
#          content={"message": f"Oops! {exc.name} did something. There goes a rainbow..."},
#     )

# @app.get("/unicorns/{name}")
# async def read_unicorn(name: str):
#     if name=="yolo":
#         raise UnicornException(name=name)
#     return {"unicorn_name":name}

@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=418, detail="Nope! I don't like 3.")
    return {"item_id": item_id}