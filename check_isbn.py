#This script checks if an input is a valid isbn number

import re
def is_valid(isbn):
    n = []
    for number in isbn:
        if number == '-':
            continue
        if re.match(r"[A-WYZ]", number):
            break
        if number == "X":
            number = "10"
        n.append(int(number))

    # The following if statement checks wheteher an isbn number is valid using the following formula:
    # (d₁ * 10 + d₂ * 9 + d₃ * 8 + d₄ * 7 + d₅ * 6 + d₆ * 5 + d₇ * 4 + d₈ * 3 + d₉ * 2 + d₁₀ * 1) mod 11 == 0
    if len(n) == 10 and 10 not in n[:9]:
        return (n[0] * 10 + n[1] * 9 + n[2] * 8 + n[3] * 7 + n[4] * 6 + n[5] * 5 + n[6] * 4 + n[7] * 3 + n[8] * 2 + n[
            9] * 1) % 11 == 0

    return False



