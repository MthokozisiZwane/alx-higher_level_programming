import unittest
from models.rectangle import Rectangle

from io import StringIO
import sys
import io


class TestRectangleAttributes(unittest.TestCase):
    def test_width_validation(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(-1, 2)
        self.assertEqual(str(cm.exception), "width must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle("invalid", 2)
        self.assertEqual(str(cm.exception), "width must be an integer")

    def test_height_validation(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(2, -1)
        self.assertEqual(str(cm.exception), "height must be > 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(2, "invalid")
        self.assertEqual(str(cm.exception), "height must be an integer")

    def test_x_validation(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(2, 2, -1, 2)
        self.assertEqual(str(cm.exception), "x must be >= 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(2, 2, "invalid", 2)
        self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_validation(self):
        with self.assertRaises(ValueError) as cm:
            r = Rectangle(2, 2, 2, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

        with self.assertRaises(TypeError) as cm:
            r = Rectangle(2, 2, 2, "invalid")
        self.assertEqual(str(cm.exception), "y must be an integer")
        
    """
    tests for the area
    """
    
    def test_area_positive(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.area(), 6)

    #def test_area_negative(self):
     #   r = Rectangle(3, -2)
      #  with self.assertRaises(ValueError):
       #     r.area()
            
    def test_area_large(self):
        r = Rectangle(1000, 1000)
        self.assertEqual(r.area(), 1000000)
        
    #def test_area_zero(self):
     #   r = Rectangle(0, 5)
      #  self.assertEqual(r.area(), 0) 
      
      
"""
      
Test disply
      
"""
class test_display_attributes(unittest.TestCase):
    
    def setUp(self):
        
        sys.stdout = io.StringIO()

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_display(self):
        r = Rectangle(3, 2)
        expected_output = "###\n###\n"
        r.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)

    def test_display_with_offset(self):
        r = Rectangle(3, 2, 2, 1)
        expected_output = "###\n###\n"
        r.display()
        self.assertEqual(sys.stdout.getvalue(), expected_output)
          
        

if __name__ == "__main__":
    unittest.main()
