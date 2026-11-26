#!/usr/bin/python3
"""Unittests for the Rectangle class."""

import io
import json
import os
import unittest
from contextlib import redirect_stdout

from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset the shared object counter before each test."""
        Base._Base__nb_objects = 0

    @staticmethod
    def _remove_file(filename):
        """Remove a test output file when it exists."""
        if os.path.exists(filename):
            os.remove(filename)

    def test_inherits_from_base(self):
        """Rectangle is a subclass of Base."""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_ids_and_attributes(self):
        """Constructor assigns ids and all attributes correctly."""
        first = Rectangle(10, 2)
        second = Rectangle(2, 10)
        third = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual([first.id, second.id, third.id], [1, 2, 12])
        self.assertEqual(third.width, 10)
        self.assertEqual(third.height, 2)
        self.assertEqual(third.x, 0)
        self.assertEqual(third.y, 0)

    def test_width_property(self):
        """The width getter and setter work with valid values."""
        rectangle = Rectangle(10, 2)
        rectangle.width = 7
        self.assertEqual(rectangle.width, 7)

    def test_height_property(self):
        """The height getter and setter work with valid values."""
        rectangle = Rectangle(10, 2)
        rectangle.height = 7
        self.assertEqual(rectangle.height, 7)

    def test_x_property(self):
        """The x getter and setter work with valid values."""
        rectangle = Rectangle(10, 2)
        rectangle.x = 5
        self.assertEqual(rectangle.x, 5)

    def test_y_property(self):
        """The y getter and setter work with valid values."""
        rectangle = Rectangle(10, 2)
        rectangle.y = 5
        self.assertEqual(rectangle.y, 5)

    def test_width_validation(self):
        """Width rejects non-integers and non-positive values."""
        for value in ["10", 10.0, None, True]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError,
                                            "width must be an integer"):
                    Rectangle(value, 2)
        for value in [0, -1]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "width must be > 0"):
                    Rectangle(value, 2)

    def test_height_validation(self):
        """Height rejects non-integers and non-positive values."""
        for value in ["2", 2.0, None, False]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError,
                                            "height must be an integer"):
                    Rectangle(10, value)
        for value in [0, -5]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "height must be > 0"):
                    Rectangle(10, value)

    def test_x_validation(self):
        """x rejects non-integers and negative values."""
        for value in ["1", 1.0, None, True]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError,
                                            "x must be an integer"):
                    Rectangle(10, 2, value)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -1)

    def test_y_validation(self):
        """y rejects non-integers and negative values."""
        for value in ["1", 1.0, None, False]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError,
                                            "y must be an integer"):
                    Rectangle(10, 2, 0, value)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 0, -1)

    def test_area(self):
        """Area returns width multiplied by height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_display_no_offset(self):
        """Display prints width hashes for each height row."""
        output = io.StringIO()
        with redirect_stdout(output):
            Rectangle(4, 3).display()
        self.assertEqual(output.getvalue(), "####\n####\n####\n")

    def test_display_with_offset(self):
        """Display honors both horizontal and vertical offsets."""
        output = io.StringIO()
        with redirect_stdout(output):
            Rectangle(2, 3, 2, 2).display()
        self.assertEqual(output.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_str(self):
        """String representation includes class, id, position, and size."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """Positional arguments update id, width, height, x, then y."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 10/10")
        rectangle.update(89, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")
        rectangle.update(89, 2, 3)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/3")
        rectangle.update(89, 2, 3, 4)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/10 - 2/3")
        rectangle.update(89, 2, 3, 4, 5)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Keyword arguments update attributes by name."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(height=1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 10/10 - 10/1")
        rectangle.update(width=1, x=2)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/10 - 1/1")
        rectangle.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 3/1 - 2/1")

    def test_update_args_ignore_kwargs(self):
        """Keyword arguments are ignored when positional args are present."""
        rectangle = Rectangle(10, 10, 10, 10, 1)
        rectangle.update(89, 2, height=99)
        self.assertEqual(str(rectangle), "[Rectangle] (89) 10/10 - 2/10")

    def test_to_dictionary(self):
        """Dictionary representation contains the expected keys."""
        rectangle = Rectangle(10, 2, 1, 9, 1)
        expected = {"x": 1, "y": 9, "id": 1, "height": 2, "width": 10}
        self.assertEqual(rectangle.to_dictionary(), expected)
        self.assertIsInstance(rectangle.to_dictionary(), dict)

    def test_save_to_file_none(self):
        """Saving None writes an empty JSON array."""
        filename = "Rectangle.json"
        self.addCleanup(self._remove_file, filename)
        Rectangle.save_to_file(None)
        with open(filename, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_to_file_empty_list(self):
        """Saving an empty list writes an empty JSON array."""
        filename = "Rectangle.json"
        self.addCleanup(self._remove_file, filename)
        Rectangle.save_to_file([])
        with open(filename, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_and_load_from_file(self):
        """Saved rectangles are reloaded with matching attributes."""
        filename = "Rectangle.json"
        self.addCleanup(self._remove_file, filename)
        originals = [Rectangle(10, 7, 2, 8, 1), Rectangle(2, 4, 0, 0, 2)]
        Rectangle.save_to_file(originals)
        with open(filename, "r", encoding="utf-8") as file:
            self.assertEqual(len(json.loads(file.read())), 2)
        loaded = Rectangle.load_from_file()
        self.assertEqual([item.to_dictionary() for item in loaded],
                         [item.to_dictionary() for item in originals])

    def test_create(self):
        """Create returns a rectangle with all attributes set."""
        rectangle = Rectangle.create(id=3, width=6, height=7, x=1, y=2)
        self.assertEqual(str(rectangle), "[Rectangle] (3) 1/2 - 6/7")


if __name__ == "__main__":
    unittest.main()
