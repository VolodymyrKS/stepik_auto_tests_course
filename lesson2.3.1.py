from selenium import webdriver
from selenium.webdriver.common.by import By
from math import log, sin
import time

# Функція для обчислення значення
def calc(x):
    return str(log(abs(12 * sin(int(x)))))

try:
    # Вказуємо шлях до драйвера вашого браузера
    driver = webdriver.Chrome()

    # 1. Відкрити сторінку
    driver.get("http://suninjuly.github.io/redirect_accept.html")

    # 2. Натиснути на кнопку
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 3. Переключитися на нову вкладку
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

    # 4. Отримати значення x та вирішити капчу
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    # 5. Ввести відповідь у поле
    input_field = driver.find_element(By.ID, "answer")
    input_field.send_keys(answer)

    # Натиснути на кнопку для відправки
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

    # Дочекаємось, щоб побачити результат
    time.sleep(10)

finally:
    # Закрити браузер після завершення
    driver.quit()
