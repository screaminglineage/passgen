# passgen
Command line password and passphrase generator 

## Contents
  1.  [Introduction](#introduction)
  2.  [Usage](#usage)
      - [Generate Passphrase](#generate-passphrase)
        - [Options](#options)
        - [Examples](#examples)
      - [Generate Password](#generate-password)
        - [Options](#options)
        - [Examples](#examples)

---

## Introduction

passgen can be used to generate a passphrase or a password in the command line.

A **passphrase** is a string of randomly generated words separated by any symbol. The separator can be anything, including a blank (no separator) or even multiple words with a space between them (The Sky's the Limit!) (or atleast as long as you enclose it within quotes). 

A **password** is just a random string of characters that can be customised to only include **uppercase**, **lowercase**, **digits** or even some **special characters**.


## Usage

The command has 2 keywords, **phrase** and **word**, which generate a passphrase and a password repectively. Some defaults are already set so simply running `passgen word` or `passgen phrase` should generate some reasonable results. However further options are avialable for fine tuning the usage.

```
usage: passgen [-h] {phrase,word} ...

Generate a password or a passphrase

options:
  -h, --help     show this help message and exit

modes available:
  to see help for the modes try "passgen phrase -h" or "passgen word -h"

  {phrase,word}
    phrase       generate a passphrase
    word         generate a password
```

  
### Generate Passphrase
```
usage: passgen phrase [-h] [-w WORD_COUNT] [-S SEPARATOR] [-c]

Generates a random series of words separated by a character
```
#### Options
The `phrase` keyword needs to be used before any of the options below.

  - `-h`, `--help` - show a help message and exit
  - `-l`, `--length` - set the length of each word in passphrase (if the length is set to something which is unavailable in the words file then it defaults back to a random letter length) [DEFAULT: **Random**]
  - `-w`, `--word-count` - set the number of words in passphrase [DEFAULT: **4**]
  - `-S`, `--separator` - set separator between each word of passphrase [DEFAULT: "**-**"]
  - `-c`, `--capitalize` - capitalize the first letter of each word in the passphrase

  
#### Examples  
  - `passgen phrase -l 6` - generates a random string of **4** (Default) words each of length **6** letters
  - `passgen phrase -w 3` - generates a random string of **3** words separated by a "**-**" such as `given-yard-slip`
  - `passgen phrase -w 5 -S "#"` - generates a random string of **5** words separated by a "**#**" such as `push#square#hall#satisfy#summer`
  - `passgen phrase -c -S "@"` - generates a random string of **4** (Default) words separated by an "**@**" with the first letter of each word capitalized such as `Concern@Imagine@Economic@Plane`

 
### Generate Password
```
usage: passgen word [-h] [-l LENGTH] [-nu] [-nl] [-nd] [-s]

Generates a random series of words separated by a character
```
#### Options
The `word` keyword needs to be used before any of the options below.

  - `-h`, `--help` - show a help message and exit
  - `-l`, `--length` - set the length of the password [DEFAULT: **50**]
  - `-nu`, `--no-uppercase` - dont allow uppercase characters in the password 
  - `-nl`, `--no-lowercase` - dont allow lowercase characters in the password 
  - `-nd`, `--no-digits` - dont allow digits in the password 
  - `-s`, `--special-chars` - allow special characters in the password 

#### Examples

  - `passgen word -l 45` - generates a random **45** character password using **uppercase**, **lowercase** and **digits** 
  - `passgen word -l 50 -nd` - generates a random **50** character password without using any **digits**
  - `passgen word -s` - generates a random **50** character password with **uppercase**, **lowercase**, **digits** and **special characters** included)
  - `passgen word -l 10 -nl -nu` - generates a random **10** character password without any **uppercase** or **lowercase** characters (ie. using only **digits**)

