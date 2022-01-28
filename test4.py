import time

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/selects2.html"
browser.get(link)

num1 = browser.find_element_by_id("num1").get_attribute("textContent")
print(num1)
num2 = browser.find_element_by_id("num2").get_attribute("textContent")
suma = int(num1) + int(num2)
print(suma)

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(suma))

button = browser.find_element_by_css_selector("button.btn").click()

time.sleep(20)
browser.quit()