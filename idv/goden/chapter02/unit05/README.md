# SQLAlchemy
## Introduction
[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) is a Python SQL Toolkit and Object Relational Mapper.

SQLAlchemy is the Python SQL toolkit and Object Relational Mapper that gives application developers the full power and flexibility of SQL. SQLAlchemy provides a full suite of well known enterprise-level persistence patterns, designed for efficient and high-performing database access, adapted into a simple and Pythonic domain language.

## Installation
When the pip is available, the distribution can be downloaded from PyPI and installed in one step:
```
pip install SQLAlchemy
```
This command will download the latest released version of SQLAlchemy from the Python Cheese Shop and install it to your system. For most common platforms, a Python Wheel file will be downloaded which provides native Cython / C extensions prebuilt.

## Addition
Additional operations can be found in below selections:
- **Create Table**<BR>https://ithelp.ithome.com.tw/articles/10282661

- **Insert, Delete and Update**<BR>https://ithelp.ithome.com.tw/articles/10282663

- **Query Table**<BR>https://ithelp.ithome.com.tw/articles/10282664

- **Examples using pytest with SQLAlchemy**<BR>https://gitlab.com/nick-hahow-demo/hahow-sqlalchemy-demo

# Mongomock

[mongomock](https://pypi.org/project/mongomock/2.3.1/) is a small library to help testing Python code that interacts with MongoDB via Pymongo. To understand what it’s useful for, we can take the following code:
```python
def increase_votes(collection):
    for document in collection.find():
        collection.update(document, {'$set' : {'votes' : document['votes'] + 1}})
```

## MongoDB Extra Information
https://gitlab.com/nick-ithelp-marathon/2023_ithelp_marathon

# Pymongo

[Pymongo](https://pypi.org/project/pymongo/) distribution contains tools for interacting with MongoDB database from Python. The bson package is an implementation of the BSON format for Python. The pymongo package is a native Python driver for MongoDB, offering both synchronous and asynchronous APIs. The gridfs package is a gridfs implementation on top of pymongo.

PyMongo supports MongoDB 4.0, 4.2, 4.4, 5.0, 6.0, 7.0, and 8.0. PyMongo follows semantic versioning for its releases.