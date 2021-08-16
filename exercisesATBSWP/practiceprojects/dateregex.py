import re

date_detect = re.compile(r'''
    (0[1-9]|[1-3][0-9])           # Dates
    (/|-|\.)                      # In-between
    (0[1-9]|1[1-2])               # Months
    (/|-|\.)                      # In-between
    ([1-2][0-9][0-9][0-9])        # Years
''', re.VERBOSE)

valid_dates = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31
}
msg = input()

date = date_detect.fullmatch(msg)

check = valid_dates.get(msg[3:5])
try:
    if int(msg[0:2]) > check:
        print("Days count exceeds month's limit.")
    else:
        print(f"{date.group()} is a valid date!")
except TypeError:
    print("Your date was invalid.")
