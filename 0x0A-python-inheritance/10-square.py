#!/usr/bin/env bash
"""Defines a class checking function."""
rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size):
        """Initialise a new square

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
