#! python3
# This program will run a bot that automatically plays the popular game 2048 in a up, right, down and left pattern continuously

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://play2048.co/')

browser.set_page_load_timeout(10)

html_elem = browser.find_element_by_tag_name('html')
i = 0
while i < 1000:
    html_elem.send_keys(Keys.LEFT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.UP)
    i += 1
