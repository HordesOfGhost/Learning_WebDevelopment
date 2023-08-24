from fastapi import FastAPI
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get('/')
def index():
    return "Welcome to Home"

# Order is important for path


@app.get('/blog/all')
def get_all_blogs():
    return {
        'message': 'All blogs provided'
    }

# Query Parameters


@app.get('/query/')
def query(page=1, page_size: Optional[int] = None):
    return {
        'message': f'All {page_size} on page {page}'
    }


@app.get('/query/{id}/comments/{comment_id}')
def get_comment(id: int, comment_id: int, value: bool = True, username: Optional[str] = None):
    return {
        'message': f'blog_id : {id}, comment_id : {id}, value : {value}, username : {username}'
    }

# Predefined paths


class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


@app.get('/blog/type/{type}')
def get_blog_type(type: BlogType):
    return {
        'message': f'Blog Type is {type}'
    }


@app.get('/blog/{id}')
def get_blog(id: int):
    return f"Id is {id}"
