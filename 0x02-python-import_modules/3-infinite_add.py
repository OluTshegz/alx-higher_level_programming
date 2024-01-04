#!/usr/bin/python3
import sys
if __name__ == "__main__":
    add = 0
    for x in range(len(sys.argv[1:])):
        add += int(sys.argv[x + 1])
    print("{}".format(add))
