#!/usr/bin/python3

def text_indentation(text):
    """
    Prints the text with 2 new lines after each '.', '?' and ':' characters.

    Args:
    text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']

    start = 0
    for i in range(len(text)):
        if text[i] in punctuation:
            print(text[start:i + 1].strip())
            print()
            start = i + 1

    if start < len(text):
        print(text[start:].strip())
