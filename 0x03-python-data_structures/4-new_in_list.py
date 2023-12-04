#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    new_list = my_list[:]

    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(new_list):
        return new_list

    # Replace the element at the specified index
    new_list[idx] = element

    return new_list


# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx = 3
    new_element = 9

    # Call the function to get a new list with the element replaced
    new_list = new_in_list(my_list, idx, new_element)

    # Print the new list and the original list
    print(new_list)
    print(my_list)
