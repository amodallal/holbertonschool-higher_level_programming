#!/usr/bin/python3
"""Module"""
from json import dumps


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(dumps(my_obj))
