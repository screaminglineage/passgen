# Default values


# Passphrase options
WORD_COUNT = 4              # Number of words in passphrase
SEPARATOR = '-'             # Passphrase separator
IS_CAPITAL = False          # Whether first letters are capitalized

# Password Options
PASSWORD_LENGTH = 20        # Number of characters in password
NO_UPPER = True             # Skip uppercase characters
NO_LOWER = True             # Skip lowercase characters
NO_DIGIT = True             # Skip digits
NO_SPECIAL = False          # Skip special characters

FILES_PATH = "files/"       # File Paths

# List of Words to use
WORDS_FILE = "words.txt"
# Uncomment the line below to use a much larger of collection of words for passphrase generation
# However Note that most of the words in this file are either uncommon or sometimes acronyms
# WORDS_FILE = "words_big.txt"



# Dont change anything below

# Print "[DEFAULT: On/Off]" in help text
default_is_capital = "On" if IS_CAPITAL else "Off"
default_no_upper = "Off" if NO_UPPER else "On"
default_no_lower = "Off" if NO_LOWER else "On"
default_no_digit = "Off" if NO_DIGIT else "On"
default_no_special = "On" if NO_SPECIAL else "Off"

