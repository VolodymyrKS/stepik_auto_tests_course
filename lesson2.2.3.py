from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Запуск браузера
browser = webdriver.Chrome()

try:
    # Відкриваємо сторінку
    browser.get("http://suninjuly.github.io/file_input.html")

    # Заповнюємо текстові поля
    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Ivanov")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("ivan@example.com")

    # Знаходимо файл і завантажуємо його
    current_dir = os.path.abspath(os.path.dirname(__file__))  # Отримуємо поточну директорію
    file_path = os.path.join(current_dir, 'text.txt')  # Шлях до файлу
    file_input = browser.find_element(By.ID, "file")
    file_input.send_keys(file_path)

    # Натискаємо кнопку "Submit"
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Чекаємо, щоб побачити результат
    time.sleep(10)

finally:
    # Закриваємо браузер
    browser.quit()
