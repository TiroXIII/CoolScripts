# This script checks if a word is an isogram
# An isogram checks if no letter is repeated in a word e.g. lumberjacks
def is_isogram(string):
    x = string.lower()
    new_list = []
    no_space_or_dash = []

    if x == "":
        return True

    for letter in x:
        if letter in ["-", " "]:
            continue
        if letter in new_list:
            break
        new_list.append(letter)
        new_str = ''.join(new_list)

    no_space_or_dash = [char for char in x if char not in ["-", " "]]
    str_only = ''.join(no_space_or_dash)

    if str_only == new_str:
        return True
    return False