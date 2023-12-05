#!/usr/bin/env python3

# The collatz conjecture is a numerical function that brings any number to 1 through a series of iterations
# if the number is even it is divided by 2
# if the number is odd it is multiplied by 3 and added by 1

"""The script below makes use of a while loop to automate the collatz conjecture
The script will run until it reaches 1
The script measures the amount of steps taken to reach the desired value of 1"""
def steps(number):
    counter = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number > 1:
            if number % 2 == 0:
                number = number/2
                counter += 1
            else:
                number = number*3 + 1
                counter += 1
        return counter