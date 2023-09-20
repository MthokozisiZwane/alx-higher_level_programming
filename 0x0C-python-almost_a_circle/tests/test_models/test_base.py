# tests/test_base.py
import unittest
import json

#from base import Base #this is for my working on spyder
from models.base import Base  #this is the line you should have in vim

class TestBase(unittest.TestCase):

    def test_create_instance_with_id(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_create_instance_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

class TestBaseToJsonString(unittest.TestCase):
    def test_empty_list(self):
        # Test when an empty list is provided
        result = Base.to_json_string([])
        self.assertEqual(result, "[]")

    def test_list_with_dicts(self):
        # Test when a list of dictionaries is provided
        dictionaries = [{'id': 1, 'name': 'Bhoke'}, {'id': 2, 'name': 'Mtho'}]
        result = Base.to_json_string(dictionaries)
        expected_result = '[{"id": 1, "name": "Bhoke"}, {"id": 2, "name": "Mtho"}]'
        self.assertEqual(result, expected_result)

    def test_with_none(self):
        # Test when None is provided
        result = Base.to_json_string(None)
        self.assertEqual(result, "[]")

if __name__ == '__main__':
    unittest.main()
