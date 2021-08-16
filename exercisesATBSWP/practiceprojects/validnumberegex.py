import re


msg = input()

num_comma_regex = re.compile(r'''
    ((\d{1,3})
    (,\d{3})*)
''', re.VERBOSE)


try:
    bob = num_comma_regex.fullmatch(msg)
    print(bob.group())
except AttributeError:
    print("There were no patterns found in your text.")