#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        dic = {}
        if cls:
            diction = self.__objects
            for key in diction:
                partition = key.replace('.', ' ')
                partition = shlex.split(partition)
                if (partition[0] == cls.__name__):
                    dic[key] = self.__objects[key]
            return (dic)
        else:
            return self.__objects

    def new(self, obj):
        """Set new object to __object to obj"""
        if obj:
            k = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path"""
        m_dict = {}
        for k, v in self.__objects.items():
            m_dict[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(m_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for k, va in (json.load(f)).items():
                    va = eval(va["__class__"])(**va)
                    self.__objects[k] = va
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """ delete an existing element
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            del self.__objects[key]

    def close(self):
        """ calls reload()
        """
        self.reload()
