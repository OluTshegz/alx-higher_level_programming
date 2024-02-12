#!/usr/bin/python3
"""This module contains Base class and some imported modules"""
import json
import os
import csv
import turtle


class Base:
    """The class Base for its instances
    Attributes:
        __nb_objects (int): Is the number of objects created from this class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """the initializing method"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list of dictionaries
        Args:
            list_dictionaries (list of dicts): The list of dictionaries
            to return it's own JSON string representation"""
        if (list_dictionaries is None or list_dictionaries == []
                or len(list_dictionaries) == 0):
            return "[]"

        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")

        for elem in list_dictionaries:
            if type(elem) is not dict:
                raise TypeError("""element in list_dictionaries
                                must be a dictionary""")

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file
        Args:
            list_objs (list): A list of instances who inherits of Base
            for example: list of Rectangle or list of Square instances"""
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", "w") as json_file:
                json_file.write("[]")
                return

        if cls.__name__ not in ["Rectangle", "Square"]:
            raise TypeError("invalid object type")

        try:
            with open(f"{cls.__name__}.json", "w") as json_file:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                list_dicts_to_json = cls.to_json_string(list_dicts)
                json_file.write(list_dicts_to_json)
        except FileNotFoundError:
            pass

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        Args:
            json_string (str): is a string representing a list of dictionaries
        """
        if json_string is None or json_string == '':
            return []
        else:
            json_string_list_dicts = json.loads(json_string)
            return json_string_list_dicts

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set
        Args:
            dictionary (dict): A dictionary that conttains all values of
            the attributes of the new instance to create"""
        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                dummy = cls(1, 1)
            elif cls.__name__ == 'Square':
                dummy = cls(1)

            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file
        The filename must be: <Class name>.json - example: Rectangle.json"""
        instances = []
        try:
            if os.path.exists(f"{cls.__name__}.json"):
                with open(f"{cls.__name__}.json", "r") as json_file:
                    content = json_file.read()

                list_dicts = cls.from_json_string(content)
                for each_dict in list_dicts:
                    instances.append(cls.create(**each_dict))
        except FileNotFoundError:
            return []

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes a list_objs to a CSV file
        Format of the CSV:
            Rectangle: <id>,<width>,<height>,<x>,<y>
            Square: <id>,<size>,<x>,<y>
        Args:
            list_objs (list): A list of instances who inherits of Base
            for example: list of Rectangle or list of Square instances
        """
        with open(f"{cls.__name__}.csv", "w") as csv_file:
            if list_objs is None or len(list_objs) == 0 or list_objs == []:
                csv.writer(csv_file).writerow([])
                return
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                elif cls.__name__ == "Square":
                    fieldnames = ["id", "size", "x", "y"]
                elif not issubclass(cls, Base):
                    raise TypeError("Incompatible object type")

                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a csv file
        The filename must be: <Class name>.csv - example: Rectangle.csv
        """
        instances = []
        try:
            file_name = "{}.csv".format(cls.__name__)
            if os.path.exists(file_name):
                with open(file_name, "r", newline="") as csv_file:
                    rows = []
                    if cls.__name__ == "Rectangle":
                        fieldnames = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        fieldnames = ["id", "size", "x", "y"]
                    elif not issubclass(cls, Base):
                        raise TypeError("Incompatible object type")

                    reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                    for row in reader:
                        for data in row:
                            row[data] = int(row[data])
                        rows.append(row)

                    instances = [cls.create(**obj) for obj in rows]
        except FileNotFoundError:
            return []

        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window and draws all the Rectangles and Squares
        Args:
            list_rectangles (list): Is the list of rectangles to be drawn
            list_squares (list): Is the list of squares to be drawn
        """
        draw_turtle = turtle.Turtle()
        draw_turtle.screen.bgcolor("green")
        draw_turtle.pensize(5)

        draw_turtle.color("blue")
        for rectangle in list_rectangles:
            draw_turtle.showturtle()
            draw_turtle.penup()
            draw_turtle.goto(rectangle.x, rectangle.y)
            draw_turtle.pendown()
            draw_turtle.forward(rectangle.width)
            draw_turtle.left(90)
            draw_turtle.forward(rectangle.height)
            draw_turtle.left(90)
            draw_turtle.forward(rectangle.width)
            draw_turtle.left(90)
            draw_turtle.forward(rectangle.height)
            draw_turtle.left(90)
            draw_turtle.hideturtle()

        draw_turtle.color("yellow")
        for square in list_squares:
            draw_turtle.showturtle()
            draw_turtle.penup()
            draw_turtle.goto(square.x, square.y)
            draw_turtle.pendown()
            draw_turtle.forward(square.size)
            draw_turtle.left(90)
            draw_turtle.forward(square.size)
            draw_turtle.left(90)
            draw_turtle.forward(square.size)
            draw_turtle.left(90)
            draw_turtle.forward(square.size)
            draw_turtle.left(90)
            draw_turtle.hideturtle()

        turtle.done()
