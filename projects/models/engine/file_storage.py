import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns dictionary of objects"""
        if cls is None:
            return self.__objects

        # prefix = f"{cls.__name__}."
        # result = {}
        # for k, v in self.__objects.items():
        #     if k.startswith(prefix):
        #         result[k] = v

        # return result

    def new(self, obj):
        """Updates the '__objects' dict"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj   # the key is the class name and id; the value is the entire object

    def save(self):
        """serializes __objects into JSON file"""
        new_dict = {}
        for id, obj in self.__objects.items():
            new_dict[id] = obj.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(new_dict, json_file) # dumping the dictionary into the file and the file handle pointing to the file

    def reload(self):
        """Deserialize the JSON file to __objects only if JSON file exits, otherwise, do nothing"""
        try:
            with open(self.__file_path, "r") as json_file: #because cant just load without opening file
                new_dict = json.load(json_file)

            for k, v in new_dict.items():
                class_name, *_ = k.split(
                    "."
                )  # split at the first instance of the dot, since its class name and id
                cls = ...
                obj = cls(v)

                self.__objects[k] = obj

        except FileNotFoundError:
            pass
