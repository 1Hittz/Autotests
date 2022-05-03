import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import math

import os

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/explicit_wait2.html'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get(link)
file_path = os.path.join(os.path.dirname(__file__), 'some.txt')

try:
    if WebDriverWait(driver, 20).until(
        ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '100')
    ) == True:
        driver.find_element(By.CSS_SELECTOR, '#book').click()
    x = calc(driver.find_element(By.CSS_SELECTOR, '#input_value').text)
    driver.find_element(By.CSS_SELECTOR, '#answer').send_keys(x)
    driver.find_element(By.CSS_SELECTOR, '#solve').click()
    print(driver.switch_to.alert.text)
    driver.switch_to.alert.accept()

finally:
    driver.quit()

