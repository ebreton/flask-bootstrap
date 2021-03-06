from flask import url_for
from hello import app


def test_urls():
    with app.test_request_context():
        assert url_for('index') == '/'
        assert url_for('hello') == '/hello'
        assert url_for('version') == '/version'


def test_version():
    with app.test_client() as client:
        resp = client.get('/version')
        assert b'Redirecting...' in resp.get_data()
