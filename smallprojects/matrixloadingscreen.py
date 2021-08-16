import random
import time

class bcolors:
    hacker_green = '\033[92m' #GREEN
    hacker_yellow = '\033[93m' #YELLOW
    RESET = '\033[0m' #RESET COLOR
    # Add colors to your hearts desire

width = 180
length = 10000000

for i in range(length):
    matrix_lst = []
    for i in range(width):
        matrix_lst.append(random.randint(0, 10))
    blank_num = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(len(matrix_lst)):
        if matrix_lst[i] in blank_num:
            matrix_lst[i] = ' '
    for i in range(len(matrix_lst)):
        if matrix_lst[i] == 0:
            print(f'{bcolors.hacker_green}{matrix_lst[i]}{bcolors.RESET}', end='')
        elif matrix_lst[i] == 1:
            print(f'{bcolors.hacker_yellow}{matrix_lst[i]}{bcolors.RESET}', end='')
        else:
            print(f'{matrix_lst[i]}', end='')
    print('')
    time.sleep(0.08)

    
