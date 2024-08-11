# Welcome To The AIRBNB Clone Project

This will be an intensive project towards building your first full web application.

## TASK 1

* Write a class called BaseModel that defines all common attributes/methods for other classes \
    Store it in models/base_model.py. That is, you will create a directory models inside projects then \
    create the file base_model.py inside models. \
* The Public Instance Attributes for BaseModel: \
    id: (string) assigned using uuid.uuid4() when an instance is created \
        we use uuid.uuid4() because we want to have unique id for each BaseModel, don't forget to convert to string  \
    created_at: (datetime) will have the value of the current datetime when an instance is created \
    updated_at: (datetime) will have the value of the current datetime when an instance is created and \
                it will be updated every time you change your object \
* Add a method `__str__`: that should print this format, `[<class name>] (<self.id>) <self.__dict__>` \
`__str__` is a special method that is used to print the unofficial representation of a class
`__repr__` is a special method that prints the official representation of a class
* Public Instance Methods:
    save(self): updates the public instance attribute `updated_at` with the current datetime
    to_dict(self): returns a dictionary containing all keys/values of `__dict__` of the instance:
        by using `self.__dict__`, only instance attributes set will be returned

        a key `__class__` must be added to this dictionary with the class name of the object

        `created_at` and `updated_at` must be converted to string object in ISO format

            the format for the date %Y-%m-%dT%H:%M:%S.%f (exp: 2017-06-14T22:31:03.285259)
            you can use isoformat() of datetime object
        this method will create a dictionary representation with “simple object type” of our BaseModel

## TASK 2

Update `__init__()` constructor method of the `models/base_model.py` file.

* `__init__(self, *args, **kwargs):`
    * `*args` will not be used
    * if `**kwargs` is not empty:
        * each key of the kwargs dictionary is an attribute name
        * each value of the kwargs dictionary is the value of this attribute name
        * ensure you convert `created_at` and `updated_at` from string to datetime object
    * otherwise:
        * create `id` and `created_at` as you did previously for every new instance

## TASK 3

Write a class `FileStorage` that serializes instances to a JSON file and deserializes JSON file to instances:

* create a new file `models/engine/file_storage.py`
* Private class attributes:
    * __file_path: (string) - path to the JSON file
    * __objects: (dictionary) - empty but will store all objects by `<class name>.id` (ex: to store a `BaseModel` object with `id=12121212`, the key will be `BaseModel.12121212`)
* Public instance methods:
    * `all(self, cls=None)`: returns the dictionary `__objects` ie. Retrieves all the instances stored in the `__objects` dictionary
    * `new(self, obj)`: sets in `__objects` the obj with key `<obj class name>.id`. Inserts a new object to my list of objects stored. `obj` is the object to be inserted into the `__object` dictionary
    * `save(self)`: serializes `__objects` to the JSON file `(path: __file_path)`. Or you can understand it as saving the objects to a file by converting the `__object` dictionary
        object to a JSON string.
    * `reload(self)`: deserializes the JSON file to `__objects` (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)


## TASK 4
* Create `models/__init__.py` file. This file will create a unique `Filestorage` instance for the application.
    * import `file_storage.py`
    * create the variable `storage` as an instance of `Filestorage`
    * call `reload()` method on this variable
* Link your `BaseModel` to `Filestorage` using the variable `storage` by updating `models/base_model.py`
    * import the variable `storage`
    * call `save(self)` method of storage
    * update `__init__(self, *args, **kwargs)`
        * if it is a new instance (not from a dictionary representation), add a call to the method `new(self)` on `storage`

## TASK 5
* Write a program called `console.py` that contains the entry point of the command interpreter. This file should be in the root of the projects directory. This file will be used to run the entire application as a command prompt.

    * Use the module `cmd`
    * Your class definition: `class AirBNBCommand(cmd.Cmd):`
    * Your command interpreter should implement quit and EOF to exit the program
    help (this action is provided by default by cmd but you should keep it updated and documented as you work through tasks)
    * a custom prompt: airbnb >>> 
    * an empty line + ENTER shouldn’t execute anything
    * Your code should not be executed when imported

## TASK 6

Some rules:

* You can assume arguments are always in the right order
* Each arguments are separated by a space
* A string argument with a space must be between double quote
* The error management starts from the first argument to the last one

Update the `console.py` to have these commands:

You will need to import `storage` from `__init__` and base model as well

* `create`: Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. Ex: `airbnb >>> create BaseModel`
    * If the class name is missing, print `** class name missing **` (ex: `airbnb >>> create`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `airbnb >>> create MyModel`)

* `show`: Prints the string representation of an instance based on the class name and `id`. Ex: `airbnb >>> show BaseModel 1234-1234-1234`
    * If the class name is missing, print `** class name missing **` (ex: `airbnb >>> show`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `airbnb >>> show MyModel`)
    * If the `id `is missing, print `** instance id missing **` (ex: `airbnb >>> show BaseModel`)
    * If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `airbnb >>> show BaseModel 121212`)

* `destroy`: Deletes an instance based on the class name and `id` (save the change into the JSON file). Ex: `airbnb >>> destroy BaseModel 1234-1234-1234`.
    * If the class name is missing, print `** class name missing **` (ex: `airbnb >>> destroy`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex:`airbnb >>> destroy MyModel`)
    * If the id is missing, print `** instance id missing **` (ex: `airbnb >>> destroy BaseModel`)
    * If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `airbnb >>> destroy BaseModel 121212`)

* `all`: Prints all string representation of all instances based or not on the class name. Ex: `airbnb >>> all BaseModel` or `airbnb >>> all`.
    * The printed result must be a list of strings (like the example below)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `airbnb >>> all MyModel`)

* `update`: Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). Ex: `airbnb >>> update BaseModel 1234-1234-1234 email "aibnb@mail.com"`.
    * Usage: `update <class name> <id> <attribute name> "<attribute value>"`
    * Only one attribute can be updated at the time
    * You can assume the attribute name is valid (exists for this model)
    * The attribute value must be casted to the attribute type
    * If the class name is missing, print `** class name missing **` (ex: `airbnb >>> update`)
    * If the class name doesn’t exist, print `** class doesn't exist **` (ex: `airbnb >>> update MyModel`)
    * If the id is missing, print `** instance id missing **` (ex: `airbnb >>> update BaseModel`)
    * If the instance of the class name doesn’t exist for the `id`, print `** no instance found **` (ex: `airbnb >>> update BaseModel 121212`)
    * If the attribute name is missing, print `** attribute name missing **` (ex: `airbnb >>> update BaseModel existing-id`)
    * If the value for the attribute name doesn’t exist, print `** value missing **` (ex: `airbnb >>> update BaseModel existing-id first_name`)
    * All other arguments should not be used (Ex: `airbnb >>> update BaseModel 1234-1234-1234 email "aibnb@mail.com" first_name "Betty"` = `airbnb >>> update BaseModel 1234-1234-1234 email "aibnb@mail.com"`)
    * `id`, `created_at` and `updated_at` cant’ be updated. You can assume they won’t be passed in the `update` command
    * Only “simple” arguments can be updated: string, integer and float. You can assume nobody will try to update list of ids or datetime
