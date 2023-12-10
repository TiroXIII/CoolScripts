# This script checks if a sentence is a panagram
# A panagram is a sentence that contains every single letter of the alphabet in it at least once

import re
import string
def is_pangram(sentence):
    x = sentence.lower()
    check_list =[]
    for char in x:
        if not re.match(r"[0-9_ .?!-,]",char):
            if char not in check_list:
                check_list.append(char)
    new = ''.join(sorted(check_list))
    if new == string.ascii_lowercase:
        return True
    return False