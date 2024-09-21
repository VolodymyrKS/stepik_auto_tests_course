from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

# Функція для обчислення математичного виразу
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Запускаємо браузер
browser = webdriver.Chrome()

try:
    # Відкриваємо сторінку
    browser.get("https://SunInJuly.github.io/execute_script.html")

    # Знаходимо значення x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    result = calc(x)

    # Використовуємо execute_script для прокручування сторінки вниз до кнопки "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("arguments[0].scrollIntoView(true);", button)

    # Вводимо відповідь у текстове поле
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(result)

    # Вибираємо чекбокс "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Використовуємо скрипт, щоб прокрутити до радіокнопки і зробити її видимою
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].scrollIntoView(true);", radiobutton)
    radiobutton.click()

    # Натискаємо кнопку "Submit"
    button.click()

    # Чекаємо, щоб побачити результат
    time.sleep(5)

finally:
    # Закриваємо браузер
    browser.quit()
