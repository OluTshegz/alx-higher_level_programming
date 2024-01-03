#!/usr/bin/python3
"""prints the ASCII alphabet except q and e,
    in lowercase, not followed by a new line."""
for alphabet in range(97, 123):
    if (alphabet != 101 and alphabet != 113):
        print("{:c}".format(alphabet), end="")
