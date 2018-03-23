from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask import flash
# flash messages must be categorized with one of
#   - [success, info, warning, danger]
# to be properly rendered with Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View, Link

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
    # activate bootstrap
    Bootstrap(app)
    # config nav
    nav = Nav()
    nav.init_app(app)
    # config storage
    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db_type = import_class_from_string(storage_type)
    db_type.init_app(app)
    return app, nav, db_type


app, nav, storage = create_app()


@app.template_filter('timeago')
def timeago(timestamp, timeago=True):
    readable = timestamp.strftime('%Y-%m-%d @%H:%M')
    if not timeago:
        return readable
    return f'<time class=timeago datetime="{str(timestamp)}">{readable}</time>'


@nav.navigation()
def main_nav():
    return Navbar(
        'Hello-Flask',
        View('Home', 'index'),
        View('Flush', 'flush', size=2),
        View('Version', 'version'),
        Link('Github', 'https://github.com/ebreton/flask-bootstrap'),
    )


@app.route('/')
def index():
    return render_template("hello.html", greetings=storage.select())


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    greeting = storage.create(request.args)
    return f"Stored & forwarded {greeting}"


@app.route('/flush/<int:size>')
def flush(size):
    flash('flushed {} greetings'.format(max(0, len(storage)-size)), category='warning')
    storage.flush(size)
    return redirect(url_for('index'))


@app.route('/version')
def version():
    flash(VERSION, category='info')
    return redirect(url_for('index'))
