# This function takes an integer with its input base and outputs the integer translated in another base
# rebase(10, 42, 3) will return 1120
def rebase(input_base, digits, output_base):
    counter = len(str(digits)) - 1
    total = 0
    for position in str(digits):
        added = int(position) * input_base ** counter
        counter -= 1
        total = total + added

    remainders_list = []
    while total > 0:
        remainder = total % output_base
        remainders_list.append(str(remainder))
        total = total // output_base
    reverse_order = remainders_list[::-1]
    return int(''.join(reverse_order))