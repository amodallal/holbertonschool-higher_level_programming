#!/usr/bin/python3
"""Module"""
from json import loads


def load_from_json_file(filename):
    """Function"""
    with open(filename, encoding='utf-8') as f:
        return loads(f.read())
