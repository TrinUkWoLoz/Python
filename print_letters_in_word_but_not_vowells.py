#!/usr/bin/python3.7

# Prompt the user to enter a word
# and assign it to the userWord variable.

userWord = input('Enter your word: ')
userWord = userWord.upper()

for letter in userWord:
    if letter in ('A', 'E', 'I', 'O', 'U'):
        continue
    elif letter:
        print(letter)
