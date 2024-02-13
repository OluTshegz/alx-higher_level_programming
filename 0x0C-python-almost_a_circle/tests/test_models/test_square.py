#!/usr/bin/python3

"""This module has TestSquare class to test the Square class"""

import unittest

from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import io
from contextlib import redirect_stdout


class TestSquare(unittest.TestCase):
    """This class is for testing Square class attributes and functions"""

    def setUp(self) -> None:
        """Setup data before each test method"""

        Base._Base__nb_objects = 0

    def test_instantiation(self):
        """Tests instantiation of the Square class"""

        sq1 = Square(5)
        self.assertEqual(sq1.id, 1)
        self.assertEqual(sq1.size, 5)
        self.assertEqual(sq1.x, 0)
        self.assertEqual(sq1.y, 0)

        self.assertTrue(isinstance(sq1, Rectangle))
        self.assertTrue(isinstance(sq1, Base))

        sq2 = Square(5, 7)
        self.assertEqual(sq2.id, 2)
        self.assertEqual(sq2.size, 5)
        self.assertEqual(sq2.x, 7)
        self.assertEqual(sq2.y, 0)

        sq3 = Square(5, 7, 4)
        self.assertEqual(sq3.id, 3)
        self.assertEqual(sq3.size, 5)
        self.assertEqual(sq3.x, 7)
        self.assertEqual(sq3.y, 4)

        sq4 = Square(5, 7, 4, 9)
        self.assertEqual(sq4.id, 9)
        self.assertEqual(sq4.size, 5)
        self.assertEqual(sq4.x, 7)
        self.assertEqual(sq4.y, 4)

        with self.assertRaises(TypeError):
            sq5 = Square()
        with self.assertRaises(TypeError):
            sq5 = Square(5, "4")
        with self.assertRaises(TypeError):
            sq5 = Square("5", 4)
        with self.assertRaises(TypeError):
            sq5 = Square(5, 4, "7")
        with self.assertRaises(ValueError):
            sq5 = Square(-1)
        with self.assertRaises(ValueError):
            sq5 = Square(0, 4)
        with self.assertRaises(ValueError):
            sq5 = Square(1, -1)
        with self.assertRaises(ValueError):
            sq5 = Square(1, 2, -1)

    def test_width(self):
        """Tests the width of the square"""

        sq = Square(10, 15)
        self.assertEqual(sq.width, 10)

        sq.width = 3
        self.assertEqual(sq.width, 3)

        with self.assertRaises(TypeError):
            sq.width = "5"

        with self.assertRaises(TypeError):
            sq.width = None

        with self.assertRaises(TypeError):
            sq.width = 1.1

        with self.assertRaises(ValueError):
            sq.width = -5

        with self.assertRaises(ValueError):
            sq.width = 0

    def test_height(self):
        """Tests the height and width of the square"""

        sq = Square(10)
        self.assertEqual(sq.height, 10)

        sq.height = 3
        self.assertEqual(sq.height, 3)

        sq.height = 7
        self.assertEqual(sq.height, 7)

        with self.assertRaises(TypeError):
            sq.height = "5"

        with self.assertRaises(TypeError):
            sq.height = None

        with self.assertRaises(TypeError):
            sq.height = 1.1

        with self.assertRaises(ValueError):
            sq.width = -5

        with self.assertRaises(ValueError):
            sq.width = 0

    def test_x(self):
        """Tests x of the square"""

        sq = Square(10, x=5)
        self.assertEqual(sq.x, 5)

        sq.x = 0
        self.assertEqual(sq.x, 0)

        with self.assertRaises(TypeError):
            sq.x = "5"

        with self.assertRaises(TypeError):
            sq.x = None

        with self.assertRaises(TypeError):
            sq.x = 1.1

        with self.assertRaises(ValueError):
            sq.x = -5

    def test_y(self):
        """Tests y of the square"""

        sq = Square(10, y=7)
        self.assertEqual(sq.y, 7)

        sq.y = 0
        self.assertEqual(sq.y, 0)

        with self.assertRaises(TypeError):
            sq.y = "5"

        with self.assertRaises(TypeError):
            sq.y = None

        with self.assertRaises(TypeError):
            sq.y = 1.1

        with self.assertRaises(ValueError):
            sq.y = -5

    def test_str(self):
        """Tests the __str__ method"""

        sq = Square(6, 2, 1, 12)
        self.assertEqual(sq.__str__(), "[Square] (12) 2/1 - 6")

        sq = Square(5, 5, 1)
        self.assertEqual(sq.__str__(), "[Square] (1) 5/1 - 5")

        sq = Square(size=7, id=15, y=3, x=4)
        self.assertEqual(sq.__str__(), "[Square] (15) 4/3 - 7")

        sq = Square(6)
        self.assertEqual(sq.__str__(), "[Square] (2) 0/0 - 6")

        sq = Square(5, 5)
        self.assertEqual(sq.__str__(), "[Square] (3) 5/0 - 5")

    def test_size(self):
        """Tests the size of the square"""

        sq = Square(10)

        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)
        self.assertEqual(sq.size, 10)

        sq.width = 7
        self.assertEqual(sq.width, 7)
        self.assertEqual(sq.height, 10)
        self.assertEqual(sq.size, 7)

        sq.height = 9
        self.assertEqual(sq.width, 7)
        self.assertEqual(sq.height, 9)
        self.assertEqual(sq.size, 7)

        sq.size = 16
        self.assertEqual(sq.width, 16)
        self.assertEqual(sq.height, 16)
        self.assertEqual(sq.size, 16)

        with self.assertRaises(ValueError):
            sq.width = 0
        with self.assertRaises(ValueError):
            sq.height = 0
        with self.assertRaises(ValueError):
            sq.size = 0
        with self.assertRaises(ValueError):
            sq.size = -5

        with self.assertRaises(TypeError):
            sq.width = "5"
        with self.assertRaises(TypeError):
            sq.height = "5"
        with self.assertRaises(TypeError):
            sq.size = "5"
        with self.assertRaises(TypeError):
            sq.size = None

    def test_display(self):
        """Tests display function"""
        sq1 = Square(2)

        output = io.StringIO()

        with redirect_stdout(output):
            sq1.display()
        self.assertEqual("##\n##\n", output.getvalue())

        output = io.StringIO()
        sq2 = Square(2, 3, 4)
        with redirect_stdout(output):
            sq2.display()
        self.assertEqual("\n\n\n\n   ##\n   ##\n", output.getvalue())

        output = io.StringIO()
        sq3 = Square(2, 4)
        with redirect_stdout(output):
            sq3.display()
        display = "    ##\n    ##\n"
        self.assertEqual(display, output.getvalue())

        sq4 = Square(3, 4, 5)
        with self.assertRaises(TypeError):
            sq4.display(1)

    def test_update(self):
        """Tests Update function that updates the attributes of an instance"""

        sq = Square(10, 10, 10)
        self.assertEqual(sq.id, 1)
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)
        self.assertEqual(sq.x, 10)
        self.assertEqual(sq.y, 10)

        sq.update(1)
        self.assertEqual(sq.id, 1)

        sq.update(89, 2)
        self.assertEqual(sq.id, 89)

        sq.update(8, 2, 3, id=7)
        self.assertEqual(sq.id, 8)

        sq.update(89, 7, 3, 4)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.width, 7)
        self.assertEqual(sq.height, 7)
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)

        sq.update(89, 2, 4, 5, id=15, x=20)
        self.assertEqual(sq.id, 89)
        self.assertEqual(sq.x, 4)

        sq.update(size=13, y=17, id=15, x=20)
        self.assertEqual(sq.size, 13)
        self.assertEqual(sq.x, 20)
        self.assertEqual(sq.y, 17)

        sq.update(id=11)
        self.assertEqual(sq.id, 11)

    def test_update_exception(self):
        """Tests exceptions thrown by the update function"""

        sq = Square(10, 10, 10, 10)

        with self.assertRaises(TypeError):
            sq.update(x="11")

        with self.assertRaises(TypeError):
            sq.update(size="h")

        with self.assertRaises(TypeError):
            sq.update(2, 1, 5, "1")

        with self.assertRaises(ValueError):
            sq.update(size=10, x=-1, y=1)

        with self.assertRaises(ValueError):
            sq.update(size=0, x=1, y=1)

        with self.assertRaises(ValueError):
            sq.update(size=-5, x=1, y=1)

    def test_to_dictionary(self):
        """Tests to_dictionary function"""

        sq1 = Square(10, 2, 1)
        sq1_dictionary = {'id': 1, 'x': 2, 'size': 10, 'y': 1}

        self.assertEqual(type(sq1_dictionary), dict)
        self.assertEqual(sq1.to_dictionary(), sq1_dictionary)

        sq2 = Square(1, 1)
        sq2_dictionary = {'size': 1, 'id': 2, 'x': 1, 'y': 0}
        self.assertEqual(sq2.to_dictionary(), sq2_dictionary)

        sq3 = Square(1)
        sq3_dictionary = {'size': 1, 'id': 3, 'x': 0, 'y': 0}
        self.assertEqual(sq3.to_dictionary(), sq3_dictionary)

        sq3 = Square(1, 1)
        sq3.update(**sq2_dictionary)
        self.assertEqual(sq3.to_dictionary(), sq2_dictionary)

        with self.assertRaises(TypeError):
            sq3.to_dictionary("1")
