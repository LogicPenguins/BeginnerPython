from selenium import webdriver
import os
import time

os.chdir('C:\\Users\\bcat4\\small-projects-python\\smallprojects')
x = 0
while x < 2:
    browser = webdriver.Firefox()
    browser.get('https://mope.io/')
    x += 1
    y = 0
    while y < 45:
        y += 1
        print(y)
        time.sleep(1)

    start_button = browser.find_element_by_css_selector('#interfacev2_root > div.home_Home__1CG4K.Home > div.home_Home__outer__1GAlz.Home__outer > div.home_Home__inner__tWhlj.Home__inner > div.home_Home__btn__1m2p7.Home__btn.home_Home__white-font__1Kba7.Home__white-font.home_Home__center__2e4Z2.Home__center.home_Home__play__3lmy6.Home__play.home_Home__rectangle__1BW4c.Home__rectangle.home_Home__green__TFDP4.Home__green')

    start_button.click()