#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage, possibly filtered by class"""
        if cls:
            class_objects = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    class_objects[key] = obj
            return class_objects
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj['__class__']
                    del obj['__class__']
                    cls = globals()[cls_name]
                    self.new(cls(**obj))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes obj from __objects if it's inside"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
