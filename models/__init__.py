#!/usr/bin/python3
'''magic method __init__'''
from os import getenv


hbnb_type_storage = getenv('HBNB_TYPE_STORAGE')
if (hbnb_type_storage == 'db'):
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
