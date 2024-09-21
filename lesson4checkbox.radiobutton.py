import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Функція для обчислення математичного виразу
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# URL сторінки
link = "https://suninjuly.github.io/math.html"

try:
    # Запускаємо браузер
    browser = webdriver.Chrome()
    browser.get(link)

    # Знаходимо значення x і обчислюємо результат
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Вводимо результат у текстове поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)

    # Клікаємо по checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Вибираємо radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    radiobutton.click()

    # Натискаємо кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Даємо час на копіювання коду
    time.sleep(10)

finally:
    # Закриваємо браузер
    browser.quit()
