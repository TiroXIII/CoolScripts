"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

import re


def value_of_card(card):
    if card == 'A':
        return 1
    if re.match(r'[2-9]', card):
        return int(card)
    if card in ['10', 'J', 'Q', 'K']:
        return 10
    return 'Enter a valid card please.'


def higher_card(card_one, card_two):
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    return card_two


def value_of_ace(card_one, card_two):
    if card_one == 'A' or card_two == 'A':
        return 1
    if value_of_card(card_one) + value_of_card(card_two) <= 10:
        return 11
    return 1


def is_blackjack(card_one, card_two):
    if re.match(r'[KQJ10]', card_one) and card_two == 'A':
        return True
    if card_one == 'A' and re.match(r'[KQJ10]', card_two):
        return True
    return False


def can_split_pairs(card_one, card_two):
    if value_of_card(card_one) == value_of_card(card_two):
        return True
    return False


def can_double_down(card_one, card_two):
    if value_of_card(card_one) + value_of_card(card_two) in [9, 10, 11]:
        return True
    return False

