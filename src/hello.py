from flask import Flask, request, render_template, redirect, flash, url_for
from utils import import_class_from_string

from settings import VERSION, APP_SECRET, STORAGE_TYPE, DATABASE_URL


def create_app(storage_type=STORAGE_TYPE):
    """ DB are usually not really relevant for proxies...

    However, one could like to know what is proxyed... The app therefore support
    - a pure python storage of the greetings received, lightning fast
    - or a more regular database through SQLAlchemy.

    The choice is made at runtime through environment variable STORAGE_TYPE:
    - in-memory storage with 'entities.storage'
    - or real DB with 'models.storage'
    """
    app = Flask(__name__)
    # config app
    app.secret_key = APP_SECRET
    # config storage
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db_type = import_class_from_string(storage_type)
    db_type.init_app(app)
    return app, db_type


app, storage = create_app()


@app.template_filter('timeago')
def timeago(timestamp, timeago=True):
    readable = timestamp.strftime('%Y-%m-%d @%H:%M')
    if not timeago:
        return readable
    return f'<time class=timeago datetime="{str(timestamp)}">{readable}</time>'


@app.route('/')
def index():
    return render_template("list.html", greetings=storage.select())


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    greeting = storage.create(request.args)
    return f"Stored & forwarded {greeting}"


@app.route('/flush/<int:size>')
def flush(size):
    flash('flushed {} greetings'.format(max(0, len(storage)-size)))
    storage.flush(size)
    return redirect(url_for('index'))


@app.route('/version')
def version():
    return VERSION
