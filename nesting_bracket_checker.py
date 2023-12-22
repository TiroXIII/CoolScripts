"""Given a string containing brackets [], braces {}, parentheses (), or any combination thereof, verify that any and
all pairs are matched and nested correctly. The string may also contain other characters, which for the purposes of
this exercise should be ignored."""

import re


def is_paired(input_string):
    check = []
    for char in input_string:
        if re.match(r'[(\[{]', char):
            check.append(char)
        elif re.match(r'[)\]}]', char):
            check.append(char)
    if (check.count('[') == check.count(']') and check.count('(') == check.count(')')
            and check.count('{') == check.count('}')):
        joined_check = ''.join(check)
        if (not re.match(r'}\{|\)\(|]\[', joined_check)
                and not re.search(r'\{]|\[}|\(}|\[\)|\{\)|\(]', joined_check)
                and not re.search(r'\(\{}]', joined_check)):
            return True
    return False
