import sys


while True:
    while True:
        input('The stuff.')
        bob = True
        while bob:
            bruh = input('GIVE ME YES OR NO: ')
            if bruh == 'y':
                print('rewinding.')
                continue
            elif bruh == 'n':
                print('Exiting.')
                sys.exit()

        bob = False
    print('Give me some stuff bro')