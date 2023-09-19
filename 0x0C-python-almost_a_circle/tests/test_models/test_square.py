
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
            
if __name__ == '__main__':
    unittest.main()
