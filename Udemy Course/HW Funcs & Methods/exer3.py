# Write a Python function that accepts a string and calculates the number of upper case
# and lowercase letters.

def case_info(string):
    num_upper = 0
    num_lower = 0
    for char in string:
        if char.islower():
            num_lower += 1
        elif char.isupper():
            num_upper += 1
    print(f'Upper Case Chars: {num_upper}\nLower Case Chars: {num_lower}')

case_info('Hello Mr. Rogers, how are you this fine Tuesday?')