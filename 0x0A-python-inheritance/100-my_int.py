#!/usr/bin/python3
""" class inheriting int"""


class MyInt(int):
    """ defining custom int class=="""
    def __eq__(self, other):
        """Override the equality operator ==."""
        return super().__ne__(other)

    """ defining !="""
    def __ne__(self, other):
        """Override the inequality operator !=."""
        return super().__eq__(other)
