import random

def gen_upper():
    '''Generates a Random Uppercase Letter'''
    return chr(random.randint(65, 90))
            
def gen_lower():
    '''Generates a Random Lowercase Letter'''
    return chr(random.randint(97, 122))

def gen_digit():
    '''Generates a Random Digit'''
    return chr(random.randint(48, 57))

def gen_special():
    '''Generates a Random Special Letter'''
    return chr(random.randint(33, 47))



def gen_password(length, allow_upper, allow_lower, allow_digit, allow_special):
    """Generates a random password"""
    password = ""
    while len(password) < length:
        choice = random.randint(1, 4)

        if choice == 1 and allow_upper:
            password += gen_upper()
        elif choice == 2 and allow_lower:
            password += gen_lower()
        elif choice == 3 and allow_digit:
            password += gen_digit()
        elif choice == 4 and allow_special:
            password += gen_special()
    return password



def gen_passphrase(filepath, word_count, separator, is_capital):
    '''Generates a list of random words from a file and then performs the
    required operations (adding capitalization and/or separator)'''
    
    with open(filepath, 'r') as words_file:
        words_list = words_file.readlines()

    # Generating random words
    passphrase_words = []
    while len(passphrase_words) < word_count:
        num = random.randint(0, (len(words_list) - 1))
        passphrase_words.append(words_list[num].strip())

    # Capitalizing first letter of each word is specified
    # Also makes all words starting with a capital letter lowercase 
    # if no capitalize option specified
    for i, word in enumerate(passphrase_words):
        if word[0][0].isupper() and is_capital is False:
            passphrase_words[i] = word.lower()
        elif is_capital is True:
            passphrase_words[i] = word.capitalize() 
    # Adding separator
    passphrase = separator.join(passphrase_words)
    return passphrase