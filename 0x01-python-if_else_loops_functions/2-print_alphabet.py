#!/usr/bin/python3
"""prints the ASCII alphabet, in lowercase, not followed by a new line."""
for alphabet in range(97, 123):
    print("{:c}".format(alphabet), end="")
