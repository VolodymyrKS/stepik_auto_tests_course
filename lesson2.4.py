from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time

# Функція для обчислення математичної задачі
def calc(x):
    return str(log(abs(12 * sin(int(x)))))

try:
    # Вказуємо шлях до драйвера
    driver = webdriver.Chrome()

    # 1. Відкрити сторінку
    driver.get("http://suninjuly.github.io/explicit_wait2.html")

    # 2. Дочекатися, коли ціна знизиться до $100 (до 12 секунд)
    WebDriverWait(driver, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 3. Натиснути кнопку "Book"
    book_button = driver.find_element(By.ID, "book")
    book_button.click()

    # 4. Отримати значення x для математичної задачі
    x_element = driver.find_element(By.ID, "input_value")
    x = x_element.text
    answer = calc(x)

    # 5. Ввести відповідь у поле
    answer_input = driver.find_element(By.ID, "answer")
    answer_input.send_keys(answer)

    # 6. Натиснути кнопку для відправки рішення
    submit_button = driver.find_element(By.ID, "solve")
    submit_button.click()

    time.sleep(10)

finally:
    # Дочекатися, щоб побачити результат, і закрити браузер
    driver.quit()
