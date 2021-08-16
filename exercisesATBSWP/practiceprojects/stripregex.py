import re


def strip_regex(x, string):
    if x == '':
        spaceLeft = re.compile(r'^\s+')
        stringLeft = spaceLeft.sub('', string)
        spaceRight = re.compile(r'\s+$')
        stringRight = spaceRight.sub('', string)
        stringBoth = spaceRight.sub('', stringLeft)
        print(stringLeft)
        print(stringRight)
    else:
        charLeft = re.compile(r'^(%s)+' % x)
        stringLeft = charLeft.sub('', string)
        charRight = re.compile(r'(%s)+$' % x)
        stringBoth = charRight.sub('', stringLeft)
    print(stringBoth)


strip_regex('Bob', 'Bob Ross is stupid')
