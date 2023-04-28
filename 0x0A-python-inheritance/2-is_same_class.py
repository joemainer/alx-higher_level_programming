#!/usr/bin/env bash
"""Defines a class checking function."""

def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of object .
    Returns:
    iF OBJECT IS EXACTLY AN INSTANCE OF A_CLASS - tRUE
    Otherwise - False.
"""

    if type(obj) == a_class:
        return True
    return False
