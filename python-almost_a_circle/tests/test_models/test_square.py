#!/usr/bin/python3
"""Unittests for the Square class."""

import io
import os
import unittest
from contextlib import redirect_stdout

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the shared object counter before each test."""
        Base._Base__nb_objects = 0

    @staticmethod
    def _remove_file(filename):
        """Remove a test output file when it exists."""
        if os.path.exists(filename):
            os.remove(filename)

    def test_inherits_from_rectangle(self):
        """Square is a subclass of Rectangle."""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_ids_and_attributes(self):
        """Constructor assigns ids and all attributes correctly."""
        first = Square(5)
        second = Square(2, 2)
        third = Square(3, 1, 3, 12)
        self.assertEqual([first.id, second.id, third.id], [1, 2, 12])
        self.assertEqual(third.size, 3)
        self.assertEqual(third.width, 3)
        self.assertEqual(third.height, 3)
        self.assertEqual(third.x, 1)
        self.assertEqual(third.y, 3)

    def test_size_property(self):
        """The size getter and setter keep width and height equal."""
        square = Square(5)
        self.assertEqual(square.size, 5)
        square.size = 10
        self.assertEqual(square.size, 10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)

    def test_size_validation(self):
        """Size uses width validation and rejects invalid values."""
        for value in ["9", 9.0, None, True]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(TypeError,
                                            "width must be an integer"):
                    Square(value)
        for value in [0, -1]:
            with self.subTest(value=value):
                with self.assertRaisesRegex(ValueError, "width must be > 0"):
                    Square(value)

    def test_area(self):
        """Area returns the size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        """Display prints a square with the correct offsets."""
        output = io.StringIO()
        with redirect_stdout(output):
            Square(3, 1, 2).display()
        self.assertEqual(output.getvalue(), "\n\n ###\n ###\n ###\n")

    def test_str(self):
        """String representation includes class, id, position, and size."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2, 0, 12)),
                         "[Square] (12) 2/0 - 2")

    def test_update_args(self):
        """Positional arguments update id, size, x, then y."""
        square = Square(5)
        square.update(10)
        self.assertEqual(str(square), "[Square] (10) 0/0 - 5")
        square.update(1, 2)
        self.assertEqual(str(square), "[Square] (1) 0/0 - 2")
        square.update(1, 2, 3)
        self.assertEqual(str(square), "[Square] (1) 3/0 - 2")
        square.update(1, 2, 3, 4)
        self.assertEqual(str(square), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """Keyword arguments update attributes by name."""
        square = Square(5)
        square.update(x=12)
        self.assertEqual(str(square), "[Square] (1) 12/0 - 5")
        square.update(size=7, y=1)
        self.assertEqual(str(square), "[Square] (1) 12/1 - 7")
        square.update(size=7, id=89, y=1)
        self.assertEqual(str(square), "[Square] (89) 12/1 - 7")

    def test_update_args_ignore_kwargs(self):
        """Keyword arguments are ignored when positional args are present."""
        square = Square(5)
        square.update(89, 2, x=99)
        self.assertEqual(str(square), "[Square] (89) 0/0 - 2")

    def test_to_dictionary(self):
        """Dictionary representation contains the expected keys."""
        square = Square(10, 2, 1, 1)
        expected = {"id": 1, "x": 2, "size": 10, "y": 1}
        self.assertEqual(square.to_dictionary(), expected)
        self.assertIsInstance(square.to_dictionary(), dict)

    def test_save_to_file_none(self):
        """Saving None writes an empty JSON array."""
        filename = "Square.json"
        self.addCleanup(self._remove_file, filename)
        Square.save_to_file(None)
        with open(filename, "r", encoding="utf-8") as file:
            self.assertEqual(file.read(), "[]")

    def test_save_and_load_from_file(self):
        """Saved squares are reloaded with matching attributes."""
        filename = "Square.json"
        self.addCleanup(self._remove_file, filename)
        originals = [Square(5), Square(7, 9, 1, 6)]
        Square.save_to_file(originals)
        loaded = Square.load_from_file()
        self.assertEqual([item.to_dictionary() for item in loaded],
                         [item.to_dictionary() for item in originals])

    def test_create(self):
        """Create returns a square with all attributes set."""
        square = Square.create(id=7, size=4, x=2, y=3)
        self.assertEqual(str(square), "[Square] (7) 2/3 - 4")


if __name__ == "__main__":
    unittest.main()
