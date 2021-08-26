import threading 
import time

print('Start of program')
def spam(person):
    time.sleep(4)
    print(f'{person} never dies.')

spam_thread = threading.Thread(target=spam, args=(['Technoblade']))
spam_thread.start()

print('Program finished praising the king.')