#!/usr/bin/python3
""" Class to add new attrinutes"""


def add_attribute(obj, attr_name, attr_value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj: The object to which the attribute should be added.
        attr_name (str): The name of the attribute to add.
        attr_value: The value of the attribute to add.

    Raises:
        TypeError: If the object can't have a new attribute.

    Example:
        class MyClass():
            pass

        mc = MyClass()
        add_attribute(mc, "name", "John")
        print(mc.name)  # Prints: John
    """
    if not hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
