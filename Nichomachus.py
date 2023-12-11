# the following script identifies whether a number is perfect, abundant, or deficient from the Nichomachus classification
def classify(number):

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors =[]
    i = 1
    while i < number:
        if number % i == 0:
            factors.append(i)
        i += 1
    total = sum(factors)
    if total == number:
        return "perfect"
    elif total < number:
        return "deficient"
    elif total > number:
        return "abundant"