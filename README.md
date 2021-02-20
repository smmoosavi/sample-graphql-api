# Sample Graphql API

In this project we create a sample Graphql API with Django and graphene

## pre-requirements

- Install [`pyenv`][pyenv] and [`poetry`][poetry]
- Install python 3.8 with pyenv, and create a new virtualenv with pyenv

```
pyenv virtualenv 3.8.3 sample-graphql-api
pyenv local sample-graphql-api 
```

## history

- Init poetry project

```
poetry init
```

- Install and init `django`

```
poetry add django
django-admin startproject api
```

[pyenv]: https://github.com/pyenv/pyenv-installer

[poetry]: https://python-poetry.org/docs/#installation