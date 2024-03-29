#!/usr/bin/python3
"""Unittest module for the user class."""

import unittest
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for user class"""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def resetStorage(self):
        """Resets user data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_8_instantiation(self):
        """Tests instantiation of User class."""
        b = User()
        self.assertEqual(str(type(b)), "<class 'models.user.User'>")
        self.assertIsInstance(b, User)
        self.assertTrue(issubclass(type(b), BaseModel))


if __name__ == "__main__":
    unittest.main()
