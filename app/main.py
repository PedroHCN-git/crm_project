from fastapi import FastAPI, Response
from app.controller import user_router

app = FastAPI()
app.include_router(user_router)

@app.get('/')
def default():
    return Response('Success', status=200)