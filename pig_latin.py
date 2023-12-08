#This script takes any phrase and converts it to pig latin
#Search the web to learn more about pig latin
#!/usr/bin/env python3

def translate(text):
    sentence = []
    for words in text.split():

        letters = [char for char in words]
        vowels = ["a", "e", "i", "o", "u"]

        if letters[0] not in vowels and letters[1] in ["y"]:
            old = letters[0:1]
            new = letters[1:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] in vowels or ''.join(letters[0:2]) in ["xr", "yt"]:
            letters.append("ay")
            pig_word = ''.join(letters)
            sentence.append(pig_word)

        elif letters[0] not in vowels and ''.join(letters[1:3]) in ["qu"]:
            old = letters[0:3]
            new = letters[3:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif ''.join(letters[0:2]) in ["qu"]:
            old = letters[0:2]
            new = letters[2:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] not in vowels and letters[1] in ["y"]:
            old = letters[0:3]
            new = letters[3:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] not in vowels and letters[2] in ["y"]:
            old = letters[0:2]
            new = letters[2:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] not in vowels and letters[1] not in vowels and letters[2] not in vowels:
            old = letters[0:3]
            new = letters[3:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] not in vowels and letters[1] not in vowels:
            old = letters[0:2]
            new = letters[2:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] not in vowels:
            old = letters[0]
            new = letters[1:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        elif letters[0] not in vowels and letters[1] in vowels:
            old = letters[0]
            new = letters[1:]
            new.extend(old)
            new.append("ay")
            pig_word = ''.join(new)
            sentence.append(pig_word)

        else:
            return False

    return ' '.join(sentence)