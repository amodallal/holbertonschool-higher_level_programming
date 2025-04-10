#!/usr/bin/python3
"""Module that defines the function lookup for introspection"""
def lookup(obj):
    """ Returns the list of available attributes and methods of an object """

    return dir(obj)
