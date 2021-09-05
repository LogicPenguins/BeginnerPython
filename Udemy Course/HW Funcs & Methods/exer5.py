# Write a Python function that checks whether a word or phrase is palindrome or not.

def palindrome(string):
    no_spaces_str = string.replace(' ', '')

    reversed_string = no_spaces_str[::-1]
    if no_spaces_str == reversed_string:
        return True
    else:
        return False


print(palindrome('nurses run'))