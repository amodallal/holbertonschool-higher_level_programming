#!/usr/bin/python3
"""Module"""
def append_write(filename="", text=""):
    """Function"""
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
