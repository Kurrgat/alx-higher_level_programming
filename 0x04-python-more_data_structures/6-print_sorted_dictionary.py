#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Sort the keys in alphabetic order
    sorted_keys = sorted(a_dictionary.keys())

    # Print the dictionary with sorted keys
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low level",
                    'ids': [1, 2, 3]}

    # Call the function to print the dictionary with sorted keys
    print_sorted_dictionary(a_dictionary)
