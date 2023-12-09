#!/usr/bin/python3

"""__init__ is a magic method for models directory"""
from models.engine.file_storage import FileStorage

file_str = FileStorage()
file_str.reload()
