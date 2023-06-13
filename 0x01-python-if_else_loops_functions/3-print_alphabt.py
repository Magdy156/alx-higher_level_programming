#!/usr/bin/python3
for lower in range(97, 123):
    if lower == 113 or lower == 101:
        continue
    print("{}".format(chr(lower)), end="")
