#!/usr/bin/env python3
import json

def serialize_and_save_to_file(data, filename):
    """
    Serializes a dictionary to a JSON file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): File path where JSON will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """
    Loads JSON data from a file and returns it as a dictionary.

    Args:
        filename (str): File path to load JSON from.

    Returns:
        dict: Deserialized dictionary from JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
