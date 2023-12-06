#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Update or add the key/value pair in the dictionary
    a_dictionary[key] = value

    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}

    # Call the function to update the dictionary
    new_dict = update_dictionary(a_dictionary, 'language', "Python")

    # Print the result
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
    print("--")
    print("--")

    # Call the function to add a new key/value pair
    new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")

    # Print the result
    print_sorted_dictionary(new_dict)
    print("--")
    print_sorted_dictionary(a_dictionary)
