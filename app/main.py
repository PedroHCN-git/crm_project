from flask import Flask, Response
from services.user_service import UserService

app = Flask()

@app.route('/', methods=['GET'])
def default():
    return Response('Success', status=200)