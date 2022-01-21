import math
from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("[id='treasure']")
    x = x_element.get_attribute("valuex")
    y = calc(x)
    #def calc(x):
        #return str(math.log(abs(12 * math.sin(int(x)))))

    option1 = browser.find_element_by_css_selector("[id='answer']")
    option1.send_keys(y)
    option2 = browser.find_element_by_css_selector("[type='checkbox']").click()
    option3 = browser.find_element_by_css_selector("[value='robots']").click()
    option4 = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()