#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        # Find the key with the maximum value
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None


if __name__ == "__main__":
    a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}

    # Call the function to get the key with the biggest integer value
    best_key = best_score(a_dictionary)

    # Print the result
    print("Best score: {}".format(best_key))

    # Call the function with an empty dictionary
    best_key = best_score({})
    print("Best score: {}".format(best_key))
