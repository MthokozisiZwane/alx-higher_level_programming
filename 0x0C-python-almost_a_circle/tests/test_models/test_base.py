# tests/test_base.py
import unittest
import json
from models.rectangle import Rectangle
#from models.base import Base


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

#test save to file
class TestSaveToFile(unittest.TestCase):

    def test_save_to_file(self):
        # Creating instances of classes
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)

        # Saving the instances to a JSON file
        Rectangle.save_to_file([r1, r2])

        # Read the contents of the saved JSON file
        with open("Rectangle.json", "r") as file:
            json_content = file.read()

        # the expected JSON representation of the objects
        expected_json = '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7},' \
                        '{"x": 0, "y": 0, "id": 2, "width": 2, "height": 4}]'

        # Convert JSON strings to sets of frozensets for comparison
        actual_set = {frozenset(item.items()) for item in json.loads(json_content)}
        expected_set = {frozenset(item.items()) for item in json.loads(json_content)}

        self.assertEqual(actual_set, expected_set)

class TestFromJsonString(unittest.TestCase):
    def test_from_json_string_empty(self):
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        json_string = '[{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 5, "height": 2}]'
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [{"id": 1, "width": 10, "height": 5}, {"id": 2, "width": 5, "height": 2}])


if __name__ == '__main__':
    unittest.main()
