# tests/test_rectangle.py
import unittest
from models.rectangle import Rectangle #this is for web terminal
#from rectangle import Rectangle #this is to test the code here in spyder

class TestRectangle(unittest.TestCase): 

    def test_create_rectangle_with_id(self):
        r = Rectangle(10, 2, id=5)
        self.assertEqual(r.id, 5)

    def test_create_rectangle_without_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(5, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)

if __name__ == '__main__':
    unittest.main()
