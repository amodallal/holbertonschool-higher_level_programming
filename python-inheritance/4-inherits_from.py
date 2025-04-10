#!/usr/bin/python3
"""Module definition"""
def inherits_from(obj, a_class):
    """function definition"""
    if isinstance(obj, a_class) and \
       issubclass(a_class, obj.__class__) is False:
        return True

    return False
