#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]  # Exclude the script name from the arguments
    result = 0

    for arg in args:
        result += int(arg)

    print(result)
