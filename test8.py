from selenium import webdriver
import time
import math

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
browser = webdriver.Chrome(options=options)

link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)




def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

button = browser.find_element_by_tag_name("button")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.new_window
#time.sleep(2)

x = browser.find_element_by_id("input_value").get_attribute('textContent')
print(x)
y = calc(int(x))

input1 = browser.find_element_by_id("answer")
input1.send_keys(y)
button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)