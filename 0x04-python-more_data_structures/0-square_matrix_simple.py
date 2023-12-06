#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix with squared values
    new_matrix = [[num ** 2 for num in row] for row in matrix]

    return new_matrix


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Call the function to get a new matrix with squared values
    new_matrix = square_matrix_simple(matrix)

    # Print the new matrix and the original matrix
    print(new_matrix)
    print(matrix)
