#! python3
# stopwatch_pretty.py - A stopwatch with well formatted text. A brotherin of the origin stopwatch python program.

import time
import pyperclip

print('Press ENTER to begin. Afterward, press ENTER to "click" the stopwatch. Press CTRL-C to quit.')
input()
print('Started.')

original_time = time.time()
last_time = original_time

lap_num = 1

try:
    while True:
        input()
        full_time = round(time.time() - original_time, 2)
        lap_time = round(time.time() - last_time, 2)
        output = f'Lap #{str(lap_num).rjust(2)}:  {str(full_time).rjust(5)} (  {str(lap_time).rjust(5)})'
        pyperclip.copy(output)
        print(output, end='')
        last_time = time.time()
        lap_num += 1
except KeyboardInterrupt:
    print('\nDone.')