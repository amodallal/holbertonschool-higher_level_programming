#!/usr/bin/python3
"""Module"""
def write_file(filename="", text=""):
    """Function"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
