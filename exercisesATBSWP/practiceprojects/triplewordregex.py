import re

triple_regex = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (|apples|cats|baseballs).', re.I)


msg = input()

bob = triple_regex.fullmatch(msg)


print(bob.group())