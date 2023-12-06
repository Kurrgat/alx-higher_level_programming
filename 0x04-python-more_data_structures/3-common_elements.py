#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    Find the common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing common elements.
    """
    return set_1 & set_2
