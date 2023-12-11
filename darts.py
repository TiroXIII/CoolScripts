# This script returns the score of a dart throw
# The dart board has an outer radius of 10, if a player throws beyond this radius they receive 0 as a score


import math

pi = math.pi

def score(x, y):
    """This is the radius of the entire dart board of which the score within this area is 1"""
    dart_board_outer = pi * 10 ** 2
    """This is the radius of the inner circle of which the score within this area is 5"""
    dart_board_inner = pi * 5 ** 2
    """This is the radius of the bulls eye of which the score within this area is 10"""
    dart_bulls_eye = pi * 1 ** 2

    dart_radius = (x ** 2 + y ** 2) ** 0.5
    dart_area = pi * dart_radius ** 2

    if dart_area > dart_board_outer:
        return 0
    if dart_board_inner < dart_area <= dart_board_outer:
        return 1
    if dart_bulls_eye < dart_area <= dart_board_inner:
        return 5
    if 0 <= dart_area <= dart_bulls_eye:
        return 10