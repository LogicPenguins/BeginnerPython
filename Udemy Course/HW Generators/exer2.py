import random

low = int(input('Low: '))
high = int(input('High: '))


def rand_num(low_param, high_param, n):
    for i in range(n):
        yield random.randint(low_param, high_param)

for num in rand_num(low, high, 20):
    print(num)

