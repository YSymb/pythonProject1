import time

from selenium import webdriver
import math
browser = webdriver.Chrome()
link = "http://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser.get(link)

x = browser.find_element_by_id("input_value").get_attribute('textContent')
print(x)
y = calc(int(x))

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
checkbox = browser.find_element_by_id("robotCheckbox").click()
radiobutt = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", radiobutt)
radiobutt.click()

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)