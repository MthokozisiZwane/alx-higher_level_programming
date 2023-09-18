# tests/test_base.py
import unittest
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

if __name__ == '__main__':
    unittest.main()
