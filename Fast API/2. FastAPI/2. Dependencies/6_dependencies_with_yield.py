from fastapi import Depends, FastAPI, HTTPException
from typing_extensions import Annotated


# async def dependency_a():
#     dep_a = generate_dep_a()
#     try:
#         yield dep_a
#     finally:
#         dep_a.close()


# async def dependency_b(dep_a: Annotated[DepA, Depends(dependency_a)]):
#     dep_b = generate_dep_b()
#     try:
#         yield dep_b
#     finally:
#         dep_b.close(dep_a)


# async def dependency_c(dep_b: Annotated[DepB, Depends(dependency_b)]):
#     dep_c = generate_dep_c()
#     try:
#         yield dep_c
#     finally:
#         dep_c.close(dep_b)



# data = {
#     "plumbus": {"description": "Freshly pickled plumbus", "owner": "Morty"},
#     "portal-gun": {"description": "Gun to create portals", "owner": "Rick"},
# }


# class OwnerError(Exception):
#     pass


# def get_username():
#     try:
#         yield "Rick"
#     except OwnerError as e:
#         raise HTTPException(status_code=400, detail=f"Owner error: {e}")


# @app.get("/items/{item_id}")
# def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
#     if item_id not in data:
#         raise HTTPException(status_code=404, detail="Item not found")
#     item = data[item_id]
#     if item["owner"] != username:
#         raise OwnerError(username)
#     return item

app = FastAPI()


class InternalError(Exception):
    pass


def get_username():
    try:
        yield "Rick"
    except InternalError:
        print("Oops, we didn't raise again, Britney 😱")
        raise


@app.get("/items/{item_id}")
def get_item(item_id: str, username: Annotated[str, Depends(get_username)]):
    if item_id == "portal-gun":
        raise InternalError(
            f"The portal gun is too dangerous to be owned by {username}"
        )
    if item_id != "plumbus":
        raise HTTPException(
            status_code=404, detail="Item not found, there's only a plumbus here"
        )
    return item_id