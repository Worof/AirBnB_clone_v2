#!/usr/bin/python3
"""Module for testing DB storage"""
import unittest
import os
from models.base_model import BaseModel
from models import storage
from models.engine.db_storage import DBStorage
from models.state import State

@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', "skip if storage type is not 'db'")
class TestDBStorage(unittest.TestCase):
    """Class to test the DB storage method"""

    @classmethod
    def setUpClass(cls):
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            cls.storage = DBStorage()
            cls.storage.reload()

    def setUp(self):
        """Set up test environment"""
        pass  # Setup actions if necessary

    def tearDown(self):
        """Clean up actions"""
        storage._DBStorage__session.rollback()

    def test_new_record(self):
        """Test if new record is added to the database"""
        initial_count = storage.count(State)
        new_state = State(name="Testland")
        new_state.save()
        final_count = storage.count(State)
        self.assertEqual(final_count, initial_count + 1)

    # Include other DB specific tests...

if __name__ == "__main__":
    unittest.main()
