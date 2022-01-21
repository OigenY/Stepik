import math
from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    option2 = browser.find_element_by_css_selector("[name='firstname']").send_keys("Ivan")
    option3 = browser.find_element_by_css_selector("[name='lastname']").send_keys("Ivan")
    option4 = browser.find_element_by_css_selector("[name='email']").send_keys("Ivan")
    import os

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'some.txt')  # добавляем к этому пути имя файла
    element=browser.find_element_by_css_selector("[type='file']")
    element.send_keys(file_path)
    option5 = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()