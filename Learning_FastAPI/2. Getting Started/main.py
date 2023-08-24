from fastapi import FastAPI

app = FastAPI()

# String Way
# @app.get('/hello')
# def index():
#     return 'Hello World'

# JSON Way
@app.get('/hello')
def index():
    return {'message' : 'Hello World!'}