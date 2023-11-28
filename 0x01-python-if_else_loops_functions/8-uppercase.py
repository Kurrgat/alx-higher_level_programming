#!/usr/bin/python3
def uppercase(s):
    upper_s = ""
    for char in s:
        if 97 <= ord(char) <= 122:
            upper_s += chr(ord(char) - 32)
        else:
            upper_s += char
    print("{:s}".format(upper_s))
