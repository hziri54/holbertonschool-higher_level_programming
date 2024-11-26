#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for row in matrix:
        for i, num in enumerate(row):
            # Print number with a space if not the last element
            print("{:d}".format(num), end=" " if i < len(row) - 1 else "")
        print()  # Move to the next line after each row
