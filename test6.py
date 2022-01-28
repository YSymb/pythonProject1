import os
from selenium import webdriver
import time
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)
input1 = browser.find_element_by_name("firstname")
input1.send_keys("Viktor")
input2 = browser.find_element_by_name("lastname")
input2.send_keys("Petrov")
input3 = browser.find_element_by_name("email")
input3.send_keys("vikpet@gma.com")

element = browser.find_element_by_id("file")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')
element.send_keys(file_path)

button = browser.find_element_by_tag_name("button")
button.click()

time.sleep(10)