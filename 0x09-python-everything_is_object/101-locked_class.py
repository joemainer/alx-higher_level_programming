#!/usr/bin/python3
"""Defines a locked class."""

class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes for anything but attributes called 'firat_name'.
    """

    __slots___ = ["first_name"]
