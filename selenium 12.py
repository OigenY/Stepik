
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    but=browser.find_element_by_css_selector("[id='book']").click()
    #button.click()
    import math

    browser.execute_script("window.scrollBy(0, 120);")

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