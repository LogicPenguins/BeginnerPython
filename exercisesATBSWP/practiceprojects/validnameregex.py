import re

name_regex = re.compile(r'([A-Z][a-z]+) Watanbe')

bob = name_regex.fullmatch('Ahanaf Watanbe')

print(bob.group())
