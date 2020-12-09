from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get('https://inventwithpython.com')

try:
    elem = browser.find_element_by_link_text('Scratch Programming Playground')
    elem.click()
except Exception as ex:
    print(ex)
