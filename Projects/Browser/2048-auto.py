from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://play2048.co/')

time.sleep(2)
# Close ad
try:
    browser.find_element_by_class_name('ezmob-footer-close').click()
except Exception as ex:
    print(ex)

htmlElem = browser.find_element_by_tag_name('html')

flag = True
while True:
    htmlElem.send_keys(Keys.ARROW_UP)
    htmlElem.send_keys(Keys.ARROW_RIGHT)
    htmlElem.send_keys(Keys.ARROW_DOWN)
    htmlElem.send_keys(Keys.ARROW_LEFT)
