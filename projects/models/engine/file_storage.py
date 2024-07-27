import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}


def all(self):
    return FileStorage.__objects

def new(self, obj):
    return f"{obj.__class__.__name__}, {obj.id}"

def save(self):
    
