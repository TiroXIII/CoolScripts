#!/usr/bin/env python3

"""The following script checks the conditions of a triangle to ensure they satisfy the mathematical rules"""
def equilateral(sides):
    if sides[0] == sides[1] == sides[2] != 0:
        return True
    return False


def isosceles(sides):
    if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]
    return False


def scalene(sides):
    if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return sides[0] != sides[1] != sides[2] != sides[0]
    return False
