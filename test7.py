from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_tag_name("button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element_by_id("input_value").get_attribute('textContent')
print(x)
y = calc(int(x))

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)
