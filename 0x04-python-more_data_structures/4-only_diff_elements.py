#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Find elements present in only one of the sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A new set containing elements unique to one of the sets.
    """
    return set_1 ^ set_2
