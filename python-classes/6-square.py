
#!/usr/bin/python3
"""Module for defining a Square class with size, position, and printing functionality."""


class Square:
    """A class that defines a square with size, position, and area calculation."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with a private size and position attributes.

        Args:
            size (int, optional): The size of the square (default is 0).
            position (tuple, optional): A tuple representing the position of the square (default is (0, 0)).
        """
        self.size = size  # Calls the setter to validate the size
        self.position = position  # Calls the setter to validate the position

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

    @property
    def position(self):
        """Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation.

        Args:
            value (tuple): A tuple representing the new position of the square.

        Raises:
            TypeError: If value is not a tuple or if the tuple does not contain two positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#' on stdout, considering position.

        If size is 0, prints an empty line. Otherwise, it prints the square with 
        the correct indentation based on the position tuple.
        """
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):  # Print vertical space for position
                print("")
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
