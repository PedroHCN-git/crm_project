from flask import Flask, Response
from app.controller import user_bp

app = Flask(__name__)
app.register_blueprint(user_bp)

@app.route('/', methods=['GET'])
def default():
    return Response('Success', status=200)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)