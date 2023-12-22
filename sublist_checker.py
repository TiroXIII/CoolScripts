"""Given any two lists A and B, determine if:

List A is equal to list B; or
List A contains list B (A is a superlist of B); or
List A is contained by list B (A is a sublist of B); or
None of the above is true, thus lists A and B are unequal"""

SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL

    len_one = len(list_one)
    len_two = len(list_two)

    if len_one < len_two:
        for i in range(len_two - len_one + 1):
            if list_two[i:i + len_one] == list_one:
                return SUBLIST

    if len_two < len_one:
        for i in range(len_one - len_two + 1):
            if list_one[i:i + len_two] == list_two:
                return SUPERLIST
    return UNEQUAL
