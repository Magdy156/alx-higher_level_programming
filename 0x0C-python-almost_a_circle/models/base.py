#!/usr/bin/python3
"""Defines a base model class"""
import json


class Base:
    """Represts a base for other classes in this project
    Private Class Attributes:
        __nb_object (int): Number of instants from the base."""

    __nb_objects = 0

    def __init__(self, id=None):
        if (id):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON str of a list of dicts.

        Args:
            list_dictionaries (list):  list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of objects"""
        with open(cls.__name__ + '.json', 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = []
                for obj in list_objs:
                    list_dicts.append(obj.to_dictionary())
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return  an instance with all attributes already set

        Args:
            **dictionary (dict): Key/value pairs to initialize
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of instances
        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                returned_val = []
                for d in list_dicts:
                    returned_val.append(cls.create(**d))
                return returned_val
        except IOError:
            return []
