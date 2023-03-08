#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
<<<<<<< HEAD
from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")
if storage_type == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
    Base = {}
=======
from os import environ

if environ.get('HBNB_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
>>>>>>> d516bb6042f1e4a01efc9a7747aef8c7c900617f
