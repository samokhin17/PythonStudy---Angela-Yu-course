# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import math
# import os
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/explicit_wait2.html"
#
#     browser = webdriver.Chrome()
#
#     browser.get(link)
#
#     WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
#     )
#     browser.find_element(By.ID, 'book').click()
#
#     num = browser.find_element(By.ID, 'input_value').text
#
#     browser.find_element(By.ID, 'answer').send_keys(calc(num))
#
#     browser.find_element(By.ID, 'solve').click()
#
s = 'My Name is Julia'

if 'Name' in s:
    print('Substring found')

index = s.find('Name')
if index != -1:
    print(f'Substring found at index {index}')
#
#
#
#
#
#
#
#
#
# finally:
#     time.sleep(10)
#     browser.quit()