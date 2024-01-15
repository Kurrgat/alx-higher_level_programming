#!/usr/bin/python3
"""
Module containing a base class for other classes, providing JSON serialization,
file handling, and drawing functionality using the turtle module.
"""

import csv
import json
import os
import turtle


class Base:
    """
    Represents the base class for all created classes.
    Provides common functionality such as JSON serialization,
    file handling, and drawing.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the base class.

        Parameters:
        - id (int): Optional id for the instance. If None, assigns a new id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string.

        Parameters:
        - list_dictionaries (list): List of dictionaries to be converted.

        Returns:
        - str: JSON string representation of the list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        if not isinstance(list_dictionaries, list)
        or not all(isinstance(i, dict) for i in list_dictionaries):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a JSON string representation to a file.

        Parameters:
        - list_objs (list): List of instances to be converted and saved.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries.

        Parameters:
        - json_string (str): JSON string to be converted.

        Returns:
        - list: List of dictionaries.
        """
        json_string_list = []

        if json_string is not None and json_string != '':
            if not isinstance(json_string, str):
                raise TypeError("json_string must be a string")
            json_string_list = json.loads(json_string)

        return json_string_list

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance with attributes set from a dictionary.

        Parameters:
        - dictionary (dict): Dictionary containing attribute values.

        Returns:
        - obj: Created instance.
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads instances from a JSON file.

        Returns:
        - list: List of instances.
        """
        file_name = cls.__name__ + ".json"
        list_of_instances = []
        list_dictionaries = []

        if os.path.exists(file_name):
            with open(file_name, 'r') as my_file:
                my_str = my_file.read()
                list_dictionaries = cls.from_json_string(my_str)
                for dictionary in list_dictionaries:
                    list_of_instances.append(cls.create(**dictionary))
        return list_of_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Saves object data to a CSV file.

        Parameters:
        - list_objs (list): List of instances to be saved.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads object data from a CSV file.

        Returns:
        - list: List of instances.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws Rectangles and Squares using the turtle module.

        Parameters:
        - list_rectangles (list): List of Rectangle instances to be drawn.
        - list_squares (list): List of Square instances to be drawn.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for _ in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for _ in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
