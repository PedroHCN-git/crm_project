from flask import Flask, Response

app = Flask()

@app.route('/', methods=['GET'])
def default():
    return Response('Success', status=200)