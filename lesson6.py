from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Запускаємо браузер
browser = webdriver.Chrome()

try:
    # Відкриваємо вказану сторінку
    browser.get("https://suninjuly.github.io/selects1.html")

    # Знаходимо елементи, які містять числа
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # Рахуємо суму
    result = int(num1) + int(num2)

    # Обираємо суму у випадаючому списку
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))  # Обираємо опцію за значенням

    # Натискаємо кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Затримка для перегляду результату
    time.sleep(5)

finally:
    # Закриваємо браузер
    browser.quit()
