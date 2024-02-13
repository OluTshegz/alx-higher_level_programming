#!/usr/bin/python3

"""This module has TestBase class to test the Base class"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import unittest
import os


class TestBase(unittest.TestCase):
    """This class is for testing Base class attributes and functions"""

    def setUp(self) -> None:
        """Setup data before each test method"""

        Base._Base__nb_objects = 0

    def test_id(self):
        """Tests the increment of the id attribute in the Base class"""

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(None)
        self.assertEqual(b3.id, 3)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b3 = Base("12")
        self.assertEqual(b3.id, "12")

        b3 = Base(id="12")
        self.assertEqual(b3.id, "12")

        b4 = Base()
        self.assertEqual(b4.id, 4)

        b5 = Base()
        self.assertEqual(b5.id, 5)
        b5.id = 15
        self.assertEqual(b5.id, 15)

        b6 = Base(7)
        self.assertEqual(b6.id, 7)

        with self.assertRaises(TypeError):
            b6 = Base(7, 4)

    def test_to_json_string(self):
        """Tests to_json_string function"""

        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(type(dictionary), dict)

        json_dictionary1 = Base.to_json_string([dictionary])

        self.assertEqual(json_dictionary1, str([dictionary]).replace("'", '"'))
        self.assertEqual(type(json_dictionary1), str)

        json_dictionary2 = Base.to_json_string([])
        self.assertEqual(type(json_dictionary2), str)
        self.assertEqual(json_dictionary2, "[]")

        json_dictionary3 = Base.to_json_string(None)
        self.assertEqual(type(json_dictionary3), str)
        self.assertEqual(json_dictionary3, '[]')

        json_dictionary4 = Base.to_json_string([{}, {}])
        self.assertEqual(json_dictionary4, "[{}, {}]")

        json_dictionary5 = Base.to_json_string([{"age": 30},
                                                {"country": "Egypt"}])
        self.assertEqual(json_dictionary5,
                         '[{"age": 30}, {"country": "Egypt"}]')

        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string(1, 5)

    def test_save_to_file(self):
        """Tests save_to_file function"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.isfile("Rectangle.json"))

        with open("Rectangle.json", "r") as file1:
            file_list1 = file1.read()

        json_dictionary1 = Rectangle.to_json_string([r1.to_dictionary(),
                                                    r2.to_dictionary()])
        self.assertEqual(json_dictionary1, file_list1)

        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file2:
            self.assertEqual(file2.read(), "[]")

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file3:
            self.assertEqual(file3.read(), "[]")

        Square.save_to_file(None)
        with open("Square.json", "r") as file6:
            self.assertEqual(file6.read(), "[]")

        sq1 = Square(10, 2, 8)
        sq2 = Square(2)
        Square.save_to_file([sq1, sq2])

        self.assertTrue(os.path.isfile("Square.json"))

        with open("Square.json", "r") as file4:
            file_list4 = file4.read()

        json_dictionary2 = Square.to_json_string([sq1.to_dictionary(),
                                                  sq2.to_dictionary()])
        self.assertEqual(json_dictionary2, file_list4)

        Square.save_to_file([])
        with open("Square.json", "r") as file5:
            self.assertEqual(file5.read(), "[]")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Square.save_to_file()

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_from_json_string(self):
        """Tests from_json_string function"""

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)

        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

        json_list_input = Square.to_json_string(list_input)
        list_output = Square.from_json_string(json_list_input)

        self.assertEqual(type(json_list_input), str)
        self.assertEqual(type(list_output), list)
        self.assertEqual(list_input, list_output)

        self.assertEqual(Rectangle.from_json_string(""), [])
        self.assertEqual(Rectangle.from_json_string(None), [])
        self.assertEqual(Rectangle.from_json_string("[{}, {}]"), [{}, {}])
        self.assertEqual(Rectangle.from_json_string("[]"), [])
        self.assertEqual(
            Rectangle.from_json_string('[{"age": 35}, {"country": "Egypt"}]'),
            [{"age": 35}, {"country": "Egypt"}])

        with self.assertRaises(TypeError):
            Rectangle.from_json_string()
        with self.assertRaises(TypeError):
            Square.from_json_string()

    def test_create(self):
        """Tests create function"""

        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(type(r2), Rectangle)
        self.assertEqual(r1_dictionary, r2.to_dictionary())
        self.assertEqual(r1.__str__(), r2.__str__())
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

        sq1 = Square(3, 5, 1)
        sq1_dictionary = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dictionary)

        self.assertEqual(type(sq1), Square)
        self.assertEqual(sq1_dictionary, sq2.to_dictionary())
        self.assertEqual(sq1.__str__(), sq2.__str__())
        self.assertIsNot(sq1, sq2)
        self.assertNotEqual(sq1, sq2)

        with self.assertRaises(TypeError):
            Square.create(sq1_dictionary)
        with self.assertRaises(TypeError):
            Rectangle.create(r1_dictionary)
        with self.assertRaises(TypeError):
            Rectangle.create(1, r1_dictionary)

    def test_load_from_file(self):
        """Tests load_from_file function"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(type(list_rectangles_output), list)
        self.assertEqual(list_rectangles_output[0].to_dictionary(),
                         r1.to_dictionary())
        self.assertEqual(list_rectangles_output[1].to_dictionary(),
                         r2.to_dictionary())

        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        list_squares_input = [sq1, sq2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(type(list_squares_output), list)
        self.assertEqual(list_squares_output[0].to_dictionary(),
                         sq1.to_dictionary())
        self.assertEqual(list_squares_output[1].to_dictionary(),
                         sq2.to_dictionary())

        with self.assertRaises(TypeError):
            Rectangle.load_from_file("file")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_save_to_file_csv(self):
        """Tests save_to_file_csv function"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])

        self.assertTrue(os.path.isfile("Rectangle.csv"))

        with open("Rectangle.csv", "r") as file1:
            file_list1 = file1.readlines()

        self.assertEqual(file_list1[0], "1,10,7,2,8\n")
        self.assertEqual(file_list1[1], "2,2,4,0,0\n")

        Rectangle.save_to_file_csv([r1])

        self.assertTrue(os.path.isfile("Rectangle.csv"))

        with open("Rectangle.csv", "r") as file1:
            file_list1 = file1.readlines()

        self.assertEqual(file_list1[0], "1,10,7,2,8\n")

        sq1 = Square(10, 2, 8)
        sq2 = Square(2)
        Square.save_to_file_csv([sq1, sq2])

        self.assertTrue(os.path.isfile("Square.csv"))

        with open("Square.csv", "r") as file2:
            file_list2 = file2.readlines()

        self.assertEqual(file_list2[0], "3,10,2,8\n")
        self.assertEqual(file_list2[1], "4,2,0,0\n")

        Square.save_to_file_csv([sq1])

        self.assertTrue(os.path.isfile("Square.csv"))

        with open("Square.csv", "r") as file2:
            file_list2 = file2.readlines()

        self.assertEqual(file_list2[0], "3,10,2,8\n")

        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file3:
            self.assertEqual(file3.read(), "\n")

        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as file3:
            self.assertEqual(file3.read(), "\n")

        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv(r1)

        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

    def test_load_from_file_csv(self):
        """Tests load_from_file_csv function"""

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(type(list_rectangles_output), list)
        self.assertEqual(list_rectangles_output[0].to_dictionary(),
                         r1.to_dictionary())
        self.assertEqual(list_rectangles_output[1].to_dictionary(),
                         r2.to_dictionary())

        sq1 = Square(5)
        sq2 = Square(7, 9, 1)
        list_squares_input = [sq1, sq2]

        Square.save_to_file_csv(list_squares_input)

        list_squares_output = Square.load_from_file_csv()

        self.assertEqual(type(list_squares_output), list)
        self.assertEqual(list_squares_output[0].to_dictionary(),
                         sq1.to_dictionary())
        self.assertEqual(list_squares_output[1].to_dictionary(),
                         sq2.to_dictionary())

        if os.path.exists("Rectangle.csv"):
            os.remove("Rectangle.csv")
        if os.path.exists("Square.csv"):
            os.remove("Square.csv")

        with self.assertRaises(TypeError):
            Rectangle.load_from_file_csv("file")

        self.assertEqual(Rectangle.load_from_file_csv(), [])
        self.assertEqual(Square.load_from_file_csv(), [])
