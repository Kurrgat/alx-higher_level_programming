#!/usr/bin/python3

def magic_calculation(a, b):
    # Import the add and sub functions from magic_calculation_102 module
    from magic_calculation_102 import add, sub

    if a < b:
        # If a is less than b, perform addition
        c = add(a, b)
        for i in range(4, 6):
            # Iterate and add numbers from 4 to 5
            c = add(c, i)
        return c
    else:
        # If a is not less than b, perform subtraction
        return sub(a, b)
