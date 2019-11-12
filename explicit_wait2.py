# Задание: ждем нужный текст на странице
# https://stepik.org/lesson/181384/step/8?unit=156009

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin

# Открыть страницу в браузере Chrome
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

# Дождаться, когда цена дома уменьшится до $100
price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

# Нажать на кнопку "Book"
book = browser.find_element(By.ID, "book").click()

# На новой странице решить капчу для роботов, чтобы получить число с ответом
x_element = browser.find_element_by_id("input_value").text


def calc(x):
    return str(log(abs(12 * sin(int(x)))))


x_result = calc(x_element)

# Ввести ответ в текстовое поле
send_answer = browser.find_element_by_id("answer").send_keys(x_result)

# Нажать кнопку "Submit"
click_button_with_result = browser.find_element_by_css_selector("button[type='submit']").click()
