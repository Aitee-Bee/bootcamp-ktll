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
* Public Instance Methods:
    save(self): updates the public instance attribute `updated_at` with the current datetime
    to_dict(self): returns a dictionary containing all keys/values of `__dict__` of the instance:
        by using `self.__dict__`, only instance attributes set will be returned
        a key `__class__` must be added to this dictionary with the class name of the object
        `created_at` and `updated_at` must be converted to string object in ISO format
            the format for the date %Y-%m-%dT%H:%M:%S.%f (exp: 2017-06-14T22:31:03.285259)
            you can use isoformat() of datetime object
        this method will create a dictionary representation with “simple object type” of our BaseModel
