#! python3
# halloween-timer.py - Will let you know when it's halloween. Until then, it'll sleep :)

import datetime
import time 


halloween2021 = datetime.datetime(2021, 10, 31, 0, 0, 0)
while datetime.datetime.now() < halloween2021:
    print('Sleeping...')
    time.sleep(1)

print('ITS HALLOWEEN!!!!')