
import unittest
import unittest.mock

from models.square import Square #use this in the shell

#from square import Square # this is for testing in spyder
import io
from io import StringIO

class TestSquare(unittest.TestCase):
    def test_size(self):
        s = Square(5)
        self.assertEqual(s.width, 5)
        
    def test_x(self):
        s = Square(5, 2)
        self.assertEqual(s.x, 2)
        
    def test_y(self):
        s = Square(5, 2, 3)
        self.assertEqual(s.y, 3)
        
        
    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)
        
    def test_the_str(self):
        s = Square(5, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (4) 2/3 - 5")
        
    def test_display(self):
        s = Square(3, 1, 1)
        expected_output = "\n ###\n ###\n ###\n"
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

"""
Testing for getter and setter methods
"""
class TestSquare2(unittest.TestCase):
    def test_size_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_size_setter(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def size_setter_with_string(self):
        s = Square(5)
        with self.assertRaises(TypeError):
            s.size = "9"

    def test_sq_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_string(self):
        s = Square(5, 2, 2, 1)
        self.assertEqual(str(s), "[Square] (1) 2/2 - 5")


        
""" Testing for def update(self, *args, **kwargs):"""


class TestSquareUpdate(unittest.TestCase):
    def test_update(self):
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.__str__(), "[Square] (10) 0/0 - 5")
        
        s1.update(1, 2)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 2")
        
        s1.update(1, 2, 3)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/0 - 2")
        
        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.__str__(), "[Square] (1) 3/4 - 2")
        
        s1.update(x=12)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/4 - 2")
        
        s1.update(size=7, y=1)
        self.assertEqual(s1.__str__(), "[Square] (1) 12/1 - 7")
        
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.__str__(), "[Square] (89) 12/1 - 7")


""" Testing the to_dictionary on square"""

class TestSquareToDictionary(unittest.TestCase):
    
    def test_to_dictionary(self):
        
        s = Square(10, 2, 1)
        s_dict = s.to_dictionary()

        expected_dict = {
            'id': 9,
            'width': 10,
            'x': 2,
            'y': 1
            }

        self.assertEqual(s_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
