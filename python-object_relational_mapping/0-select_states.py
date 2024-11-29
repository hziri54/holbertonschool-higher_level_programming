#!/usr/bin/python3
"""Defines a text function."""

def text_indentation(text):
    """Print text with 2 new lines after the characters ., ? and :"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Skip leading spaces
        if text[i] == ' ':
            i += 1
            continue

        # Print characters until ., ?, or :
        print(text[i], end="")

        # If ., ?, or : found, print two new lines
        if text[i] in ".?:":
            print("\n")
            i += 1

            # Skip spaces after punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue

        i += 1
