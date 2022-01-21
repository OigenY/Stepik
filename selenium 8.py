import math
from selenium import webdriver
from selenium.webdriver.support.ui import Select


import time
try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x,y):
       return str(str(int(x)+int(y)))

    x_element = browser.find_element_by_css_selector("[id='num1']")
    x = x_element.text
    y_element = browser.find_element_by_css_selector("[id='num2']")
    y = y_element.text
    ara = calc(x,y)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(ara)  # ищем элемент с текстом "Python"
    #def calc(x):
        #return str(math.log(abs(12 * math.sin(int(x)))))
    option4 = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()