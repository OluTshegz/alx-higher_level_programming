#!/usr/bin/python3

"""This module has TestRectangle class to test the Rectangle class"""

import unittest

from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """This class is for testing Rectangle class attributes and functions"""

    def setUp(self) -> None:
        """Setup data before each test method"""

        Base._Base__nb_objects = 0

    def test_instantiation(self):
        """Tests instantiation of the Rectangle class"""

        r1 = Rectangle(5, 7)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 5)
        self.assertEqual(r1.height, 7)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r2 = Rectangle(5, 7, 4)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r2.width, 5)
        self.assertEqual(r2.height, 7)
        self.assertEqual(r2.x, 4)
        self.assertEqual(r2.y, 0)

        r3 = Rectangle(5, 7, 4, 9)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 5)
        self.assertEqual(r3.height, 7)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 9)

        r4 = Rectangle(5, 7, 4, 9, 15)
        self.assertEqual(r4.id, 15)
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 7)
        self.assertEqual(r4.x, 4)
        self.assertEqual(r4.y, 9)

        r4 = Rectangle(5, 7, 4, 9, [15])
        self.assertEqual(r4.id, [15])
        self.assertEqual(r4.width, 5)
        self.assertEqual(r4.height, 7)
        self.assertEqual(r4.x, 4)
        self.assertEqual(r4.y, 9)

        with self.assertRaises(TypeError):
            r5 = Rectangle()
        with self.assertRaises(TypeError):
            r5 = Rectangle(5)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, "4")
        with self.assertRaises(TypeError):
            r5 = Rectangle("5", 4)
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 4, "7")
        with self.assertRaises(TypeError):
            r5 = Rectangle(5, 4, 7, "8")

    def test_width(self):
        """Tests the width of the rectangle"""

        r = Rectangle(10, 15)
        self.assertEqual(r.width, 10)

        r.width = 3
        self.assertEqual(r.width, 3)

        with self.assertRaises(TypeError):
            r.width = "5"

        with self.assertRaises(TypeError):
            r.width = None

        with self.assertRaises(TypeError):
            r.width = 1.1

        with self.assertRaises(ValueError):
            r.width = -5

        with self.assertRaises(ValueError):
            r.width = 0

    def test_height(self):
        """Tests the height of the rectangle"""

        r = Rectangle(10, 15)
        self.assertEqual(r.height, 15)

        r.height = 3
        self.assertEqual(r.height, 3)

        with self.assertRaises(TypeError):
            r.height = "5"

        with self.assertRaises(TypeError):
            r.height = None

        with self.assertRaises(TypeError):
            r.height = 1.1

        with self.assertRaises(ValueError):
            r.height = -5

        with self.assertRaises(ValueError):
            r.height = 0

    def test_x(self):
        """Tests x of the rectangle"""

        r = Rectangle(10, 15, x=5)
        self.assertEqual(r.x, 5)

        r.x = 0
        self.assertEqual(r.x, 0)

        with self.assertRaises(TypeError):
            r.x = "5"

        with self.assertRaises(TypeError):
            r.x = None

        with self.assertRaises(TypeError):
            r.x = 1.1

        with self.assertRaises(ValueError):
            r.x = -5

    def test_y(self):
        """Tests y of the rectangle"""

        r = Rectangle(10, 15, y=7)
        self.assertEqual(r.y, 7)

        r.y = 0
        self.assertEqual(r.y, 0)

        with self.assertRaises(TypeError):
            r.y = "5"

        with self.assertRaises(TypeError):
            r.y = None

        with self.assertRaises(TypeError):
            r.y = 1.1

        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        """Tests the area of the rectangle"""

        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

        r.width = 2
        r.height = 10
        self.assertEqual(r.area(), 20)

        r.width = 7
        r.height = 8
        self.assertEqual(r.area(), 56)

    def test_str(self):
        """Tests the __str__ method"""

        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r.__str__(), "[Rectangle] (12) 2/1 - 4/6")

        r = Rectangle(5, 5, 1)
        self.assertEqual(r.__str__(), "[Rectangle] (1) 1/0 - 5/5")

        r = Rectangle(height=3, width=7, id=15, y=3, x=4)
        self.assertEqual(r.__str__(), "[Rectangle] (15) 4/3 - 7/3")

        r = Rectangle(5, 5)
        self.assertEqual(r.__str__(), "[Rectangle] (2) 0/0 - 5/5")

    def test_update(self):
        """Tests Update function that updates the attributes of an instance"""

        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89, 2)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89, 2, 3, id=7)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)

        r.update(89, 2, 3, 4)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 10)

        r.update(89, 2, 3, 4, 5)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        r.update(89, 2, 3, 4, 5, id=15, x=20)
        self.assertEqual(r.id, 89)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

        r.update(width=13, height=10, y=17, id=15, x=20)
        self.assertEqual(r.id, 15)
        self.assertEqual(r.width, 13)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 20)
        self.assertEqual(r.y, 17)

        r.update(id=11)
        self.assertEqual(r.id, 11)

    def test_update_exception(self):
        """Tests exceptions thrown by the update function"""

        r = Rectangle(10, 10, 10, 10)

        with self.assertRaises(TypeError):
            r.update(x="11")

        with self.assertRaises(TypeError):
            r.update(height="h")

        with self.assertRaises(TypeError):
            r.update(2, 2, 1, 5, "1")

        with self.assertRaises(ValueError):
            r.update(width=10, height=15, x=-1, y=1)

        with self.assertRaises(ValueError):
            r.update(width=0, height=15, x=1, y=1)

        with self.assertRaises(ValueError):
            r.update(width=10, height=-5, x=1, y=1)

    def test_to_dictionary(self):
        """Tests to_dictionary function"""

        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = {'id': 1, 'width': 10, 'height': 2, 'x': 1, 'y': 9}

        self.assertEqual(type(r1_dictionary), dict)
        self.assertEqual(r1.to_dictionary(), r1_dictionary)

        r2 = Rectangle(1, 1)
        r2_dictionary = {'width': 1, 'id': 2, 'x': 0, 'height': 1, 'y': 0}
        self.assertEqual(r2.to_dictionary(), r2_dictionary)

        r3 = Rectangle(1, 1)
        r3.update(**r2_dictionary)
        self.assertEqual(r3.to_dictionary(), r2_dictionary)

        with self.assertRaises(TypeError):
            r4 = Rectangle()
        with self.assertRaises(TypeError):
            r5 = Rectangle("2", 4)
        with self.assertRaises(TypeError):
            r6 = Rectangle(2, "4")
        with self.assertRaises(ValueError):
            r7 = Rectangle(-2, "4")
        with self.assertRaises(ValueError):
            r8 = Rectangle(2, 0)
        with self.assertRaises(TypeError):
            r9 = Rectangle("2", 0)
