# passgen
Command line password and passcode generator 

## Contents
  1.  [Introduction](#introduction)
  2.  [Usage](#usage)
---

## Introduction

passgen can be used to generate a passcode, or a string of randomly generated words separated by any symbol. The separator can be anything including a blank (no separator) or just some white space (as long as it is enclosed within quotes while entering).


## Usage
```
usage: passgen [-h] [-v] [-s SEPARATOR] [-c] [length]

Generate a random series of words separated by a character

positional arguments:
  length                specify the number of words (DEFAULT: 4)

options:
  -h, --help            show this help message and exit
  -v, --verbose         display more text as output
  -s SEPARATOR, --separator SEPARATOR
                        character to separate each word (DEFAULT: "-")
  -c, --capitalize      capitalize the first character of each word (DEFAULT: Off))
```

  
### Options with Examples
  
  - `length` - set the number of words in the passcode [DEFAULT: **4**]
  - `-v`, `--verbose` - will passcode in the format `Generated Passcode: <Passcode>`
  - `-s`, `--separator` - denote the word-separator in the pass code [DEFAULT: "**-**"]
  - `-c`, `--capitalize` - capitalize the first letter of each word in the passcode
  
Examples - 
  - `passgen 3` - will output a random string of **3** words separated by a "**-**" such as `given-yard-slip`
  - `passgen 5 -s "#"` - will output a random string of **5** words separated by a "**#**" such as `push#square#hall#satisfy#summer`
  - `passgen -c -s "@"` - will output a random string of **4** (Default) words separated by an "**@**" with the first letter of each word capitalized such as `Concern@Imagine@Economic@Plane`

 
