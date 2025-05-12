#!/usr/bin/env python3
import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serializes the current object to a file using pickle.
        If serialization fails, nothing is written.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Silent fail as per instructions

    @classmethod
    def deserialize(cls, filename):
        """
        Deserializes an object from a file.
        Returns:
            CustomObject instance if successful, else None
        """
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            pass
        return None

