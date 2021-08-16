import re

checks = [
    [re.compile(r'[a-z]+'), 'Must contain a lower case letter.'],
    [re.compile(r'[A-Z]+'), 'Must contain a capital letter.'],
    [re.compile(r'\d+'), 'Must contain a digit.'],
    [re.compile(r'.{8,}'), 'Password too short.'],
]


def strong_password_detect(password):
    for regex, message in checks:
        if regex.search(password) is None:
            print(message)
            return
    print("Strong password.")


user_password = input()
strong_password_detect(user_password)