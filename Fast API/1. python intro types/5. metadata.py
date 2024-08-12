from typing import Annotated

def say_hello(name: Annotated[str, "this is a metadata"]) -> str:
    return f"Hello {name}"


print(say_hello("BIBEK"))