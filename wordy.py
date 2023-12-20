import re
#Problem derived from extreme_startup on Github
#The script takes a math problem as a string and solves it
def answer(question):
    if re.search(r'\b(?:cubed|squared|root)\b', question) or re.search(r'\b(?:Who|Where|When|Why)\b', question):
        raise ValueError('unknown operation')
    if not re.search(r'\b(?:plus|minus|divided|multiplied|\d+)\b', question):
        raise ValueError('syntax error')
    convert = [word.rstrip('?.!') for word in question.split()]
    new = []
    for word in convert:
        if re.match(r'-?[0-9]', word):
            new.append(word)
        if word == 'plus':
            word = '+'
            new.append(word)
        if word == 'minus':
            word = '-'
            new.append(word)
        if word == 'divided':
            word = '/'
            new.append(word)
        if word == 'multiplied':
            word = '*'
            new.append(word)
        else:
            continue
    try:
        result = float(new[0])
    except ValueError as e:
        raise ValueError('syntax error')
    for i in range(1, len(new), 2):
        operator = new[i]
        try:
            operand = float(new[i + 1])
        except IndexError as e:
            raise ValueError('syntax error')
        except ValueError as e:
            raise ValueError('syntax error')
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '/':
            result /= operand
    return result

