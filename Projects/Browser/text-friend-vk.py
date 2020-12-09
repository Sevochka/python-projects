import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pyinputplus as pyip
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://vk.com')

# Получение элементов ввода пароля и email
try:
    emailField = driver.find_element_by_id('index_email')
    passField = driver.find_element_by_id('index_pass')
except Exception as ex:
    print(ex)

# Создание email и пароля для аунтефикации
email = 'vsevoiodkochnev@mail.ru'
password = pyip.inputStr('Ваш пароль: ')


# Заполнение инпутов
emailField.send_keys('vsevoiodkochnev@mail.ru')
passField.send_keys(password)
passField.submit()

WebDriverWait(driver, 10).until(lambda d: d.title == 'Security Check | VK')
try:
    confirmationCode = driver.find_element_by_id('authcheck_code')
    sendBtn = driver.find_element_by_id('login_authcheck_submit_btn')
except Exception as ex:
    print(ex)

confirmation = pyip.inputStr('Ваш код подтверждения: ')
confirmationCode.send_keys(confirmation)
sendBtn.click()

WebDriverWait(driver, 10).until(lambda d: d.title == 'News')

friendsLink = driver.find_element_by_css_selector('#l_fr > a')
friendsLink.click()

# friendName = driver.find_element_by_xpath(
#     '//div[@class="friends_user_info friends_user_info--fullRow"]/div/a[contains(text(),"Alexey")]/text()')

WebDriverWait(driver, 10).until(lambda d: d.title.find('Friends') != -1)
try:
    friendName = driver.find_element_by_partial_link_text('Mikhail')
except Exception as ex:
    print(ex)

friendName.click()

WebDriverWait(driver, 10).until(lambda d: d.title.find('Friends') != -1)

writeMsg = driver.find_element_by_css_selector('#profile_message_send > div > a.button_link.cut_left')
writeMsg.click()