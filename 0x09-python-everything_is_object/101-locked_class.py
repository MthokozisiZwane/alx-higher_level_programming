#!/usr/bin/python3

"""prevents the user from dynamically creating new instance attributes"""


class LockedClass:
    """ method to prevent creation og new instance"""
    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no\
                                 attribute '{}'".format(name))
