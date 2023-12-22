# This script takes an input string and creates a rotational cipher based on a key
# If the string is 'a' and the key is one, a will become b
# If the string is 'millionaire' and the key is 13, the string will become 'zyvvbanver'

import re


def rotate(text, key):
    t = []
    for letter in text:
        if re.match(r"[0-9 .,?_!-']", letter):
            t.append(letter)
            continue
        if 97 <= ord(letter) + key <= 122 and letter.islower():
            v = ord(letter) + key
            t.append(chr(v))
        if ord(letter) + key > 122 and letter.islower():
            v = ord(letter) + key - 26
            t.append(chr(v))
        if 65 <= ord(letter) + key <= 90 and letter.isupper():
            v = ord(letter) + key
            t.append(chr(v))
        if ord(letter) + key > 90 and letter.isupper():
            v = ord(letter) + key - 26
            t.append(chr(v))

    return ''.join(t)
