#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    # Create a new dictionary with values multiplied by 2
    new_dict = {key: value * 2 for key, value in a_dictionary.items()}

    return new_dict


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}

    # Call the function to get a new dictionary with values multiplied by 2
    new_dict = multiply_by_2(a_dictionary)

    # Print the sorted dictionaries before and after the multiplication
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)
