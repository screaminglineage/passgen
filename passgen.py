#!/usr/bin/env python

import random
import argparse

# Default values
LENGTH = 4                  # Number of words in passcode
SEPARATOR = '-'             # Passcode separator
IS_CAPITAL = False          # Whether first letters are capitalized
FILES_PATH = "files/"       # File Paths

# List of Words to use
WORDS_FILE = "words.txt"
# Uncomment the line below to use a much larger of collection of words for generation
# Note that most of the words in the file are either uncommon or sometimes acronyms
#WORDS_FILE = "words_big.txt"


def gen_passcode(filepath, length, separator, is_capital):
    '''Generates a list of random words from a file and then performs the
    required operations (adding capitalization and/or separator)'''
    
    with open(filepath, 'r') as words_file:
        words_list = words_file.readlines()

    # Generating random words
    passcode_words = []
    while len(passcode_words) < length:
        num = random.randint(0, (len(words_list) - 1))
        passcode_words.append(words_list[num].strip())

    # Capitalizing first letter of each word
    if is_capital:
        for i, word in enumerate(passcode_words):
            passcode_words[i] = passcode_words[i].capitalize() 
    passcode = separator.join(passcode_words)
    return passcode


# Argparser get command line options
def get_args():
    parser = argparse.ArgumentParser(description='Generate a random series of words separated by a character')

    # Gets Comand Line Arguments
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='display only passcode')

    parser.add_argument('length', type=int, nargs='?', default = LENGTH,
                        help=f'specify the number of words (DEFAULT: {LENGTH})')

    parser.add_argument('-s', '--separator', type=str, default = SEPARATOR,
                        help=f'character to separate each word (DEFAULT: "{SEPARATOR}")')

    default_is_capital = "On" if IS_CAPITAL else "Off"
    parser.add_argument('-c', '--capitalize', action='store_true', default = IS_CAPITAL,
                        help=f'capitalize the first character of each word (DEFAULT: {default_is_capital}))')

    args = parser.parse_args()
    return args


def main(args):
    passcode = gen_passcode(f"{FILES_PATH}{WORDS_FILE}", args.length,
                            args.separator, args.capitalize)
    # Displays only the passcode if quiet mode is turned on
    if args.quiet:
        print(passcode)
    else:
        print('Generated Passcode:', passcode)

main(get_args())


