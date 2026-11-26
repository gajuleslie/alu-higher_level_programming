#!/usr/bin/python3
"""Unittests for the Base class."""

import json
import os
import unittest

from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the shared object counter before each test."""
        Base._Base__nb_objects = 0

    def test_id_none_increments(self):
        """Generated ids increase from one when no id is given."""
        first = Base()
        second = Base()
        third = Base()
        self.assertEqual([first.id, second.id, third.id], [1, 2, 3])

    def test_id_explicit(self):
        """An explicit id is assigned without using the counter."""
        explicit = Base(12)
        generated = Base()
        self.assertEqual(explicit.id, 12)
        self.assertEqual(generated.id, 1)

    def test_to_json_string_none_and_empty(self):
        """Empty input produces an empty JSON array string."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_list(self):
        """A list of dictionaries becomes a JSON string."""
        dictionaries = [{"id": 1, "name": "one"}, {"id": 2, "name": "two"}]
        result = Base.to_json_string(dictionaries)
        self.assertIsInstance(result, str)
        self.assertEqual(json.loads(result), dictionaries)

    def test_from_json_string_none_and_empty(self):
        """Empty JSON strings produce empty lists."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_list(self):
        """A JSON string becomes a list of dictionaries."""
        string = '[{"id": 1, "name": "one"}]'
        self.assertEqual(Base.from_json_string(string),
                         [{"id": 1, "name": "one"}])

    def test_create_sets_all_attributes(self):
        """Create applies a dictionary to a new instance."""
        rectangle = Rectangle.create(id=8, width=3, height=4, x=1, y=2)
        self.assertEqual(rectangle.id, 8)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)

    def test_load_from_file_missing(self):
        """Missing JSON files produce an empty instance list."""
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_save_and_load_from_file(self):
        """Saved instances are reloaded with matching attributes."""
        filename = "Rectangle.json"
        self.addCleanup(self._remove_file, filename)
        original = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([original])
        self.assertTrue(os.path.exists(filename))
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0].to_dictionary(),
                         original.to_dictionary())

    @staticmethod
    def _remove_file(filename):
        """Remove a test output file when it exists."""
        if os.path.exists(filename):
            os.remove(filename)


if __name__ == "__main__":
    unittest.main()
