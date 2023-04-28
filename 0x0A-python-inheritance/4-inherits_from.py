#!/usr/bin/env bash
"""Defines a class checking function."""

def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object is to check.
        a_class (type): The class is to match the type of obj to.
    Returns:
        If obj is an iherited instance of a-class - True.
    Otherwise - False
    """
    if issubclass(type(obj), a_class)and type(obj) != a_class:
        return True
    return False
