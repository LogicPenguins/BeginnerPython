def sequence(num):
    modified_num = num
    while modified_num != 1:
        if modified_num % 2 == 0:
            modified_num /= 2
        else:
            modified_num *= 3
            modified_num += 1
    print(f'{num} failed the collatz sequence')

for i in range(1000000000000):
    sequence(i+1)