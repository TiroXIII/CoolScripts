#!/usr/bin/env python3

# This script will output if a given year is a leap year from the Gregorian calendar definition

"""The following script checks if a year is evenly divisible by 4 as well as being evenly
evenly divisible by both 100 and 400"""
"""In addition the script checks if a year is merely evenly divisble by 4 while not being 
evenly divisible by 100"""

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return True
    if year % 4 == 0 and not year % 100 == 0:
        return True
    return False
