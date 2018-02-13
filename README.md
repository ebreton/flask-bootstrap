<!-- markdownlint-disable -->
<h1 align="center" style="margin:1em">
  <img src="./docs/static/logo.png"
       alt="Flask Bootstrap"
       width="200">
  <p>Flask bootstrap</p>
</h1>

<h4 align="center">
  Offer yourselv a head start for your next flask app
</h4>

<p align="center">
  <a href="https://github.com/ebreton/flaskbootstrap/blob/master/docs/CHANGELOG.md">
    <img src="https://img.shields.io/github/release/ebreton/flaskbootstrap.svg"
         alt="Changelog">
  </a>
  <a href="https://travis-ci.org/ebreton/flaskbootstrap">
    <img src="https://travis-ci.org/ebreton/flaskbootstrap.svg?branch=master"
         alt="Travis">
  </a>
  <a href="https://codecov.io/gh/ebreton/flaskbootstrap">
    <img src="https://codecov.io/gh/ebreton/flaskbootstrap/branch/master/graph/badge.svg"
         alt="Codecov" />
  </a>
  <a href="https://github.com/ebreton/flaskbootstrap/blob/master/LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-blue.svg"
         alt="License" />
  </a>
</p>
<br>
 
### Main features

- **Dev friendly**: A Makefile will allow to quickly setup the dev environment. The application can be run locally with hot reloading of the code, or without. With DB or without. Emulating Heroku context or not. `make deploy` will push the app online.
- **Out-of-the-box** deployment to Heroku
- **Support for DB**... but... **not mandatory**. 
- **Configuration through environement variables** in a `.env` file: mainly for Heroku, and storage type.
- **Automated** testing and deployment: connected to Travis and Codecov, relies on Heroku toolbelt for deployment.
- **Comes with a basic frontend** 

### You said 'optionnal' DB?

If persistent storage is needed: will use postgreSQL with Heroku by default. Also works without DB, in which case the data will be stored in memory, until next restart of the application

### Something is missing ?

Head to [githup issues](https://github.com/ebreton/flaskbootstrap/issues) and submit one ! Be sure to have a look at the [CONTRIBUTING.md](./docs/CONTRIBUTING.md) guide before

## Install and Usage

Check out [INSTALL.md](./docs/INSTALL.md) for more details

## Changelog

All notable changes to this project are documented in [CHANGELOG.md](./docs/CHANGELOG.md).

## Contribution

Check out [CONTRIBUTING.md](./docs/CONTRIBUTING.md) for more details

As well as our [CODE_OF_CONDUCT.md](./docs/CODE_OF_CONDUCT.md), where we pledge to making participation in our project and our community a harassment-free experience for everyone
