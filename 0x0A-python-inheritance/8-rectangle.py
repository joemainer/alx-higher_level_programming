#!/usr/bin/env bash
"""Defines a class checking function."""
basegeometry = __Import__('7-base_geometry').BaseGeometry

class Rectangle(Basegeometry):
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Initialise a new rectangle.

        Args:
            width )int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """

    self.integer_validator("width", width)
    self.__width = width
    self.integer_validtor("height", height)
    self.__height = height
