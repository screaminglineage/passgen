#!/usr/bin/python
import random
import argparse

# Default values
FILES_PATH = "files/"
WORDS_FILE = "words.txt"

# Uncomment the line below to use a much 
# larger of collection of words for generation
# Note that most of the words in the file are  
# either uncommon or sometimes acronyms
#WORDS_FILE = "words_big.txt"


def gen_passcode(length=4, separator=' ', capitalize=False):
    '''Opens a file containing the list of words to be used and
    adds them to the passcode until the number of words added is equal to
    the length passed when calling the function.'''

    with open(f"{FILES_PATH}{WORDS_FILE}", 'r') as words_file:
        word_count = 0          # Counts no. of words in passcode
        passcode = ''           # Stores passcode
        words_list = words_file.readlines()

        while word_count < length:
            # Random number which corresponds to a list index of a word
            num = random.randint(0, (len(words_list) - 1))

            for i in range(len(words_list)):
                if num == i:
                    # Capitalizes the first letter of each word in passcode
                    if capitalize:
                        word = words_list[i].strip().capitalize()
                    else:
                        word = words_list[i].strip()

                    # Joins the words together with separator in between each
                    passcode += word + separator
                    # Increments word counter to count no. of words in passcode
                    word_count += 1

    # Deletes the last character from passcode as it's a trailing separator character
    return passcode[:-1]


parser = argparse.ArgumentParser(
         description='Generate a random series of words separated by a character')

# Gets Comand Line Arguments
parser.add_argument('-q', '--quiet', action='store_true',
                    help='display only passcode')

parser.add_argument('length', type=int, nargs='?',
                    help='specify the number of words (DEFAULT: 4) ')

parser.add_argument('-s', '--separator', default='-', type=str,
                    help='character to separate each word (DEFAULT: "-")')

parser.add_argument('-c', '--capitalize', action='store_true',
                    help='capitalize the first character of each word')



args = parser.parse_args()

# Sets the length to 4 by default if no value is entered
if args.length is None:
    length = 4
else:
    length = args.length

# Turns off capitalization by default if no value is entered
if args.capitalize:
    capitalize = True
else:
    capitalize = False

passcode = gen_passcode(length, args.separator, capitalize)

# Displays only the passcode if quiet mode is turned on
if args.quiet:
    print(passcode)
else:
    print('Generated Passcode:', passcode)





