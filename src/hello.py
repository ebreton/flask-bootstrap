from flask import Flask

from settings import VERSION


app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/hello')
def hello():
    return b'Hello, World'


@app.route('/version')
def version():
    return VERSION
