#!/usr/bin/python3
"""Function to print a square with # characters."""


def print_square(size):
    """Print a square of size `size` with # characters.

    Args:
        size (int): The size of the square.

    Raises:
        TypeError: If size is not an integer or is a float less than 0.
        ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    
    for _ in range(size):
        print('#' * size)
