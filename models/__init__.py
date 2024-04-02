#!/usr/bin/python3
"""This module instantiates an appropriate storage type according to the HBNB_TYPE_STORAGE environment variable"""
from os import getenv
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

if getenv('HBNB_TYPE_STORAGE') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
