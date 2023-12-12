# This script takes a list as input and changes it to a new list after undergoing mathematical rebasing
# The script makes use of raise statements to create ValueErrors for incorrect inputs

def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    for test in digits:
        if input_base <= test or test < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    counter = len(digits) - 1
    total = 0
    if sum(digits) == 0 or digits == []:
        return [0]
    for position in digits:
        added = position * input_base**counter
        counter -= 1
        total += added
    total
    remainders_list = []
    while total >= 1:
        remainder = total % output_base
        remainders_list.append(remainder)
        total = total//output_base
    reverse_order = remainders_list[::-1]
    return reverse_order