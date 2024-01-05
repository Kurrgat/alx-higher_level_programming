#!/usr/bin/python3
"""This defines a locked class"""


class LockedClass:
    """Only allow the creation of 'first_name' attribute"""
    __slots__ = ('first_name',)
