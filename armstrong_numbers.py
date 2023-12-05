#!/usr/bin/env python3

# This script takes a number as input and checks to see if it is an armstrong number
# An Armstrong number is a number that is equal in value to the sum of its digits to a factor of its length
# 9 = 9^1 and 153 = 1^3 + 5^3 + 3^3 (both Armstrong numbers)

"""The function below converts the number to a string so that its length can be determined from the len function.
The function then splits the number into a list of integers.
The function then iterates over the contents of the list(group) and performs the power function using the factor variable
The total_sum is calculated at the end of the loop and is compared to the number used as input
If the numbers are equal in value, the function returns True and proves the number is an Armstrong number"""
def is_armstrong_number(number):
    int_to_str = str(number)
    factor = len(int_to_str)
    group = [int(digit) for digit in int_to_str]

    total_sum = 0
    for i in group:
        total_sum += i ** factor

    return total_sum == number