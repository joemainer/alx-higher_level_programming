#!/usr/bin/env bash
"""Defines a class checking function."""

def is_kind_of _class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class

    Args:
        obj (any): The object is to check.
        a_class (type): The class match the type ofobj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Oherwise - False.
    """
    If isinstance(obj, a_class):
        return True
    return False
