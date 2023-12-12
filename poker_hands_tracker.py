"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(round_1, round_2):
    return round_1 + round_2

def list_contains_round(rounds, number):
    if number in rounds:
        return True
    return False

def card_average(hand):
    return sum(hand) / len(hand)

def approx_average_is_average(hand):
    avg1 = (hand[0] + hand[-1]) / 2
    position = (len(hand) / 2) - 0.5
    avg2 = hand[int(position)]
    if card_average(hand) == avg2 or card_average(hand) == avg1:
        return True
    return False

def average_even_is_average_odd(hand):
    even = []
    odd = []
    place = 0
    while place < len(hand):
        if place % 2 == 0:
            even.append(hand[place])
        else:
            odd.append(hand[place])
        place += 1
    if card_average(odd) == card_average(even):
        return True
    return False

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
