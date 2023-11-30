#!/usr/bin/python3
if __name__ == "__main__":
    """Print the sum, difference, multiple, and quotient of 10 and 5."""
    # Import the required functions from calculator_1.py
    from calculator_1 import add, sub, mul, div

    # Assign values to variables a and b
    a = 10
    b = 5

    # Perform addition and print the result
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Perform subtraction and print the result
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Perform multiplication and print the result
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Perform division and print the result
    print("{} / {} = {}".format(a, b, div(a, b)))
