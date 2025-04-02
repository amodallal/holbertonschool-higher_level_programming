#!/usr/bin/python3
"""Module for defining a Square class with printing functionality."""


class Square:
    """A class that defines a square."""

    def __init__(self, size=0):
        """Initialize the square with a private size attribute.

        Args:
            size (int, optional): The size of the square (default is 0).
        """
        self.size = size  # Calls the setter to validate the size

    @property
    def size(self):
        """Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character '#' on stdout.

        If size is 0, it prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print('#' * self.__size)
