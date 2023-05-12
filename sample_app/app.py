import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    custom_message = os.environ.get('CUSTOM_MESSAGE', 'Hello, World!')
    return custom_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
