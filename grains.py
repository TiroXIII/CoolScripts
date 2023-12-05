#!/usr/bin/env python3
# This is a Python script that solves a mathematical equation for doubling grains on a chess board
# A single grain is placed on square one, and is doubled in the next preceding square
# The chess board has 64 squares

"""This function works out how many grains would be found on a particular square on the chess board
and takes into account that the input cannot be 0, None, negative, or greater than 65"""
def square(number):
    if number not in range(1, 65) or number == None:
        raise ValueError("square must be between 1 and 64")
    result = 2 ** (number - 1)
    print(result)
    return result

"""This function works out the total number of grains accumulated if the process was allowed
to start at the first square and iterate until the last square"""
def total():
    sum = 0
    for x in range(1, 65):
        number = 2 ** (x - 1)
        sum += number
    print(sum)
    return (sum)