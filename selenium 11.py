import math
from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    opt = browser.find_element_by_css_selector("[type='submit']").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    import math

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_css_selector("[id='input_value']")
    x = x_element.text
    y = calc(x)
    #def calc(x):
        #return str(math.log(abs(12 * math.sin(int(x)))))


    option1 = browser.find_element_by_css_selector("[id='answer']")
    option1.send_keys(y)
    #option2 = browser.find_element_by_css_selector("[type='checkbox']").click()
    #option3 = browser.find_element_by_css_selector("[value='robots']").click()
    option4 = browser.find_element_by_css_selector("[type='submit']").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()