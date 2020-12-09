from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://login.metafilter.com')
userElem = browser.find_element_by_id('user_name')
userElem.send_keys('Vsevolod')

passwordElem = browser.find_element_by_id('user_pass')
passwordElem.send_keys('1123231231231')
passwordElem.submit()