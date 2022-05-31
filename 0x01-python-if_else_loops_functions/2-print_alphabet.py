#!/usr/bin/python3
#Program that prints the ASCII alphabet, in lowercase, not followed by a new line.
for letter in range(97, 123):
    print("{:c}".format(letter),end="")
