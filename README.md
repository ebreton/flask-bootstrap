<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  <img src="./docs/static/logo.png"
       alt="Flask Bootstrap"
       width="200">
</h1>

<h4 align="center">
  Offer yourself a head start <br /> for your next flask app
</h4>

<p align="center">
  <a href="https://github.com/ebreton/flask-bootstrap/blob/master/docs/CHANGELOG.md">
    <img src="https://img.shields.io/github/release/ebreton/flask-bootstrap.svg"
         alt="Changelog">
  </a>
  <a href="https://travis-ci.org/ebreton/flask-bootstrap">
    <img src="https://travis-ci.org/ebreton/flask-bootstrap.svg?branch=master"
         alt="Travis">
  </a>
  <a href="https://codecov.io/gh/ebreton/flask-bootstrap">
    <img src="https://codecov.io/gh/ebreton/flask-bootstrap/branch/master/graph/badge.svg"
         alt="Codecov" />
  </a>
  <a href="https://github.com/ebreton/flask-bootstrap/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg"
         alt="License" />
  </a>
</p>
<br>

### Looking for something lighter ?

Like a bootstrap for a simple new python project with a simple CLI ? Check [PyBootstrap](https://github.com/ebreton/pybootstrap)...

### Main features

- **Dev friendly**: a Makefile will allow to quickly setup everything with `make init-venv`
- **Multiple runners**:
  - Ran locally with hot reloading of the code with `make deploy`
  - Or still locally, but a step closer to production with `make gunicorn`
  - Or emulating Heroku context with `make heroku`
  - Or even hosted on Heroku with `make deploy`
  - All this... with or without DB :balloon:
- **Support for DB** thanks to [flask-SQLalchemy](http://flask-sqlalchemy.pocoo.org/2.3/)... but... **not mandatory**. 
- **Configuration through environement variables** in a `.env` file: mainly for Heroku, and storage type.
- **Automated** testing and deployment: connected to Travis and Codecov, relies on Heroku toolbelt for deployment.
- **Support for Bootstrap3**, thanks to [flask-bootstrap](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html)
- **Easy creation of your navigation** with [flask-nav](http://pythonhosted.org/flask-nav/)
- **Comes with a basic frontend**, from the bootstrap example ['sticky footer with fixed navbar'](https://getbootstrap.com/docs/3.3/examples/sticky-footer-navbar/)

#### You said 'optionnal' DB?

If persistent storage is needed: will use postgreSQL with Heroku by default. Also works without DB, in which case the data will be stored in memory, until next restart of the application

#### Something is missing ?

Head to [githup issues](https://github.com/ebreton/flask-bootstrap/issues) and submit one ! Be sure to have a look at the [CONTRIBUTING.md](./docs/CONTRIBUTING.md) guide before

### Install and Usage

Check out [INSTALL.md](./docs/INSTALL.md) for more details

### Changelog

All notable changes to this project are documented in [CHANGELOG.md](./docs/CHANGELOG.md).

### Contribution

Check out [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for more details

As well as our [CODE_OF_CONDUCT.md](./docs/CODE_OF_CONDUCT.md), where we pledge to making participation in our project and our community a harassment-free experience for everyone
