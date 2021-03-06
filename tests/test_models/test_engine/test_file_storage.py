#!/usr/bin/python3
"""
Unittest for file_storage
"""
import pep8
import models
import os.path
import unittest
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

F_storage = FileStorage()
B_model = BaseModel()
object = storage.all()


class TestFileStorage(unittest.TestCase):
    """ Write unittests for the class FileStorage. """

    def test_pep8_conformance(self):
        """ Test that we conform to PEP8. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_all(self):
        """ Test that checks the all method. """
        self.assertEqual(type(object), dict)
        self.assertTrue(hasattr(F_storage, 'all'), True)
        self.assertIs(object, storage.__FileStorage__objects)

    def test_new(self):
        """ Test that checks the new method. """
        B_model.name = 'Da_Sa'
        self.assertEqual(B_model.name, 'Da_Sa')
        self.assertTrue(hasattr(storage, 'new'), True)
        self.assertEqual(type(B_model), models.base_model.BaseModel)

    def test_save(self):
        """ Test that checks the save method. """
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(F_storage, 'save'), True)
        self.assertEqual(os.path.isfile('file.json'), True)
        self.assertGreater(B_model.updated_at, B_model.created_at)

    def test_reload(self):
        """ Test that checks the reload method. """
        self.assertTrue(hasattr(F_storage, 'reload'), True)

    def test_FileStorage_empty(self):
        """ Test that checks the empty FileStorage. """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertEqual(type(FileStorage()), FileStorage)


if __name__ == '__main__':
    unittest.main()
