# Functions to help edit strings

def capitalize_title(title):
    capital = title.title()
    return capital

def check_sentence_ending(sentence):
    if sentence.endswith("."):
        return True
    return False

def clean_up_spacing(sentence):
    cleaned = sentence.strip()
    return cleaned

def replace_word_choice(sentence, old_word, new_word):
    replaced = sentence.replace(old_word, new_word)
    return replaced
