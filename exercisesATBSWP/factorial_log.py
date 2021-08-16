import logging
from pathlib import Path


logging_file = Path(f'{Path.home()}\\VSCPythonProjects\\logs\\testlog.txt')

logging.basicConfig(filename=logging_file, level=logging.DEBUG, 
format='%(asctime)s - %(levelname)s - %(message)s')


logging.debug('Debugging started.')

for i in range(10):
    num = i * 5
    num *= 3
    num /= 4
    logging.debug(f'Num is currently: {num}')

logging.debug('Debugging finished.')
