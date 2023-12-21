"""The Atbash cipher is a simple substitution cipher that relies on transposing all the letters in the alphabet such that the resulting alphabet is backwards. The first letter is replaced with the last letter, the second with the second-last, and so on.

An Atbash cipher for the Latin alphabet would be as follows:

Plain:  abcdefghijklmnopqrstuvwxyz
Cipher: zyxwvutsrqponmlkjihgfedcba
It is a very weak cipher because it only has one possible key, and it is a simple mono-alphabetic substitution cipher. However, this may not have been an issue in the cipher's time.

Ciphertext is written out in groups of fixed length, the traditional group size being 5 letters, leaving numbers unchanged, and punctuation is excluded. This is to make it harder to guess things based on word boundaries. All text will be encoded as lowercase letters.

"""

import re

alphabet_dict = {'a': 25, 'b': 23, 'c': 21, 'd': 19, 'e': 17, 'f': 15, 'g': 13, 'h': 11, 'i': 9, 'j': 7, 'k': 5, 'l': 3,
                 'm': 1, 'n': -1, 'o': -3, 'p': -5, 'q': -7, 'r': -9, 's': -11, 't': -13, 'u': -15, 'v': -17, 'w': -19,
                 'x': -21, 'y': -23, 'z': -25}

def encode(plain_text):
    decode = []
    for letter in plain_text:
        if re.match(r'[\d+]', letter):
            decode.append(letter)
        elif re.match(r'[\.\?\!\'\,]', letter):
            continue
        elif re.match(r'[a-z]', letter):
            code = alphabet_dict[letter]
            new_letter = chr(ord(letter) + code)
            decode.append(new_letter)
        elif re.match(r'[A-Z]', letter):
            tran = letter.lower()
            code = alphabet_dict[tran]
            new_letter = chr(ord(tran) + code)
            decode.append(new_letter)
    decode_string = ''.join(decode)
    result = [decode_string[i:i + 5] for i in range(0, len(decode_string), 5)]
    return ' '.join(result)

def decode(ciphered_text):
    space_stripped = ciphered_text.replace(' ', '')
    encode = []
    for letter in space_stripped:
        if re.match(r'[\d+]', letter):
            encode.append(letter)
        elif re.match(r'[a-z]', letter):
            code = alphabet_dict[letter]
            code *= -1
            for key, value in alphabet_dict.items():
                if value == code:
                    encode.append(key)
    encode_string = ''.join(encode)
    return encode_string