#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Pad the tuples with zeros if they are smaller than 2 elements
    tuple_a = tuple_a + (0, 0)[:2 - len(tuple_a)]
    tuple_b = tuple_b + (0, 0)[:2 - len(tuple_b)]

    # Take only the first 2 elements of each tuple and add them
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple


if __name__ == "__main__":
    tuple_a = (1, 89)
    tuple_b = (88, 11)

    # Add two tuples
    new_tuple = add_tuple(tuple_a, tuple_b)
    print(new_tuple)

    # Add tuple_a with a smaller tuple (1 element)
    print(add_tuple(tuple_a, (1, )))

    # Add tuple_a with an empty tuple
    print(add_tuple(tuple_a, ()))
