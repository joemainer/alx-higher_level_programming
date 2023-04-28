#!/usr/bin/env bash
"""Defines a class checking function."""

def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add tp onj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise typeError("can't add new attribute")
    setattr(obj, att, value)
