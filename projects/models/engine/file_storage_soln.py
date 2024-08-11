#!/usr/bin/python3
"""
A module that serializes an object into a JSON format,
saves it to a file and also deserializes the file back
into a Python dictionary.
"""
import json


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
        return self.__objects
    
    def new(self, obj):
        """
        Insert or update the objects dict with the
        obj param
        """
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj
    
    def save(self):
        """
        Serialize the objects dict
        """
        # data = {key: self.__objects[key].to_dict() for key in self.__objects.keys()}

        data = {}
        for key in self.__objects:
            data[key] = self.__objects[key].to_dict()
        
        with open(self.__file_path, "w+") as file:
            json.dump(data, file)
    
    def reload(self):
        """
        Deserializes JSON file into a Python dict
        """
        try:
            with open(self.__objects) as file:
                for obj in json.load(file).values():
                    name = obj['__class__']
                    del obj["__class__"]
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            pass


obje = FileStorage()
