#!/usr/bin/env bash
"""Defines a class checking function."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represent a square"""

    def __init__(self, size)
    """initialize anew square.

    Args:
        size (int): The size of the new square;
        """
        self.integer_validtor("size", size)
        super().__init__(size, size)
        self.__size = size
