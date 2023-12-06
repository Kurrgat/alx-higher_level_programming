#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    # Check if the key exists before deleting
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'Number': 89, 'track': "Low",
                    'ids': [1, 2, 3]}

    # Call the function to delete the specified key
    new_dict = simple_delete(a_dictionary, 'track')

    # Print the sorted dictionaries before and after the deletion
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
    print("--")
    print("--")

    # Call the function with a key that doesn't exist
    new_dict = simple_delete(a_dictionary, 'c_is_fun')

    # Print the sorted dictionaries before and after the attempted deletion
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
