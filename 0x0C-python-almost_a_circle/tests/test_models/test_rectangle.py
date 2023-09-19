import unittest
from models.rectangle import Rectangle
#from rectangle2 import Rectangle #this line only works on spyder

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

if __name__ == "__main__":
    unittest.main()
