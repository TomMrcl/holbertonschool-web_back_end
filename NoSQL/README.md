# NoSQL

## Description

This project introduces NoSQL databases, focusing on MongoDB. It covers basic
operations such as creating, reading, updating, and deleting documents using
both the MongoDB shell and the PyMongo library in Python.

## Requirements

### MongoDB Scripts

- All scripts will be interpreted on Ubuntu 20.04 LTS
- All files should end with a new line
- The first line of all files should be a comment: `// my comment`
- MongoDB version 4.2

### Python Scripts

- Python 3.9
- Ubuntu 20.04 LTS
- pycodestyle 2.5.*
- PyMongo 4.x
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- All modules should have a documentation
- All functions should have a documentation
- All functions and coroutines must be type-annotated

## Setup

### Install MongoDB 4.2 on Ubuntu 20.04

```bash
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo service mongod start
```

### Install PyMongo

```bash
pip3 install pymongo
```

## Files

### MongoDB Shell Scripts

#### 0-list_databases

Lists all databases in MongoDB.

```bash
cat 0-list_databases | mongo
```

#### 1-use_or_create_database

Creates or switches to the database `my_db`.

```bash
cat 1-use_or_create_database | mongo
```

#### 2-insert

Inserts a document with the attribute `name` set to "Holberton school" into
the collection `school`.

```bash
cat 2-insert | mongo my_db
```

#### 3-all

Lists all documents in the collection `school`.

```bash
cat 3-all | mongo my_db
```

#### 4-match

Lists all documents where `name` equals "Holberton school" in the collection
`school`.

```bash
cat 4-match | mongo my_db
```

#### 5-count

Displays the number of documents in the collection `school`.

```bash
cat 5-count | mongo my_db
```

#### 6-update

Adds the attribute `address` with the value "972 Mission street" to all
documents where `name` equals "Holberton school" in the collection `school`.

```bash
cat 6-update | mongo my_db
```

#### 7-delete

Deletes all documents where `name` equals "Holberton school" in the collection
`school`.

```bash
cat 7-delete | mongo my_db
```

### Python Scripts

#### 8-all.py

Contains the function `list_all(mongo_collection)` that lists all documents
in a collection. Returns an empty list if no documents are found.

#### 9-insert_school.py

Contains the function `insert_school(mongo_collection, **kwargs)` that inserts
a new document in a collection based on the provided keyword arguments.
Returns the new document `_id`.

#### 10-update_topics.py

Contains the function `update_topics(mongo_collection, name, topics)` that
updates all topics of a school document matching the given name.

#### 11-schools_by_topic.py

Contains the function `schools_by_topic(mongo_collection, topic)` that returns
the list of schools that teach a specific topic.

#### 12-log_stats.py

A script that provides statistics about Nginx logs stored in MongoDB. It
displays the total number of logs, the count of each HTTP method, and the
number of status check requests.

Example output:

```text
94778 logs
Methods:
method GET: 93842
method POST: 229
method PUT: 0
method PATCH: 0
method DELETE: 0
47415 status check
```

## Key Concepts

### What is NoSQL

NoSQL refers to database management systems that do not use the traditional
relational table model. They are designed to handle large volumes of
unstructured or semi-structured data and offer flexible schemas.

### What is MongoDB

MongoDB is a document-oriented NoSQL database that stores data as BSON
(Binary JSON) documents. It allows for flexible and scalable data storage
without requiring a fixed schema.

### Difference between SQL and NoSQL

SQL databases are relational, table-based, and use structured query language
with a fixed schema. NoSQL databases are non-relational, can store documents,
key-value pairs, graphs, or wide columns, and offer dynamic schemas suited for
large-scale or unstructured data.

### CRUD Operations in MongoDB

- Create: `insertOne()`, `insertMany()`
- Read: `find()`, `findOne()`
- Update: `updateOne()`, `updateMany()` with `$set`
- Delete: `deleteOne()`, `deleteMany()`

## Author

Holberton School student
