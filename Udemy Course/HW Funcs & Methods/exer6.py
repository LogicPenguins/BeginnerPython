# Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    ns_str = str1.replace(' ', '')
    letters = 0
    str_lst = list(ns_str.lower())
    alphabet_checks = 0
    for char in str_lst:
        if char in alphabet:
            alphabet = alphabet.replace(char, '')
            alphabet_checks += 1
    if alphabet_checks == 26:
        print(f'Your sentence had {alphabet_checks} letters. It is a pangram!')
    else:
        print(f'Your sentence had {alphabet_checks} letters. It was not a pangram.')


ispangram('The quick brown fox jumps over the lazy dog')

# Or you can do this

import string

def ispangram(str1, alphabet=string.ascii_lowercase):

    alphaset = set(alphabet)

    str1 = str1.replace(" ", "")
    str1 = str1.lower()
    str1 = set(str1)

    if alphaset == str1:
        print("Match.")
    else:
        print("Nope.")

ispangram("The quick brown fox umps over the lazy dog")