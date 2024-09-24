#!/usr/bin/python3
"""
A module that serializes an object into a JSON format,
saves it to a file and also deserializes the file back
into a Python dictionary.
"""
import json
from models.base_model_soln import BaseModel


class FileStorage:
    """
    Serializes instance of a class and also deserialize
    the JSON object back into a Python dictionary
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """
        Retrieves all the instances stored
        """
        return FileStorage.__objects
    
    def new(self, obj):
        """
        Insert or update the objects dict with the
        obj param
        """
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
    
    def save(self):
        """
        Serialize the objects dict
        """
        # data = {key: self.__objects[key].to_dict() for key in self.__objects.keys()}

        with open(FileStorage.__file_path, 'w+') as f:
            data = {}
            data.update(FileStorage.__objects)
            for key, val in data.items():
                data[key] = val.to_dict()
            json.dump(data, f)
    
    def reload(self):
        """
        Deserializes JSON file into a Python dict
        """
        classes = {"BaseModel": BaseModel}
        try:
            data = {}
            with open(FileStorage.__file_path, 'r') as f:
                data = json.load(f)
                for key, val in data.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass
