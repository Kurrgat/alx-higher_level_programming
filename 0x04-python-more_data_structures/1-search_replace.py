#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Create a new list with replaced elements
    new_list = [replace if item == search else item for item in my_list]

    return new_list


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]

    # Call the function to get a new list with replaced elements
    new_list = search_replace(my_list, 2, 89)

    # Print the new list and the original list
    print(new_list)
    print(my_list)
