# def get_full_name(first_name:str, last_name:str):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name

# print(get_full_name("john", "doe"))


# def get_name_with_age(name: str, age: int):
#     name_with_age = name + " is this old: " + str(age)
#     return name_with_age

# get_name_with_age('bibek',12)

# Union
# 3.10 + 


# def process_item(item: int | str):
#     print(item)

# from typing import Union

# def process_item(item: Union[int, str]):
#     print(item)

# process_item(12)
# process_item('12')


# optional
# 3.10+

# def say_hi(name: str | None = None):
#     if name is not None:
#         print(f"Hey {name}!")
#     else:
#         print("Hello World")

# from typing import Optional

# def say_hi(name: Optional[str] = None):
#     if name is not None:
#         print(f"Hey {name}")
#     else:
#         print("Not Given Name")

# say_hi('Bibek')

# from typing import Optional


# def say_hi(name: Optional[str]):
#     print(f"Hey {name}!")