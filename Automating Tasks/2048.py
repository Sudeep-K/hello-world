#! python3

# 2048.py -  a simple game where you combine tiles by sliding them up, down, left,
# or right with the arrow keys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# open browser using selenium and open the '2048' page
browser = webdriver.Firefox()
browser.get('https://play2048.co/')

# find the element 'html' to give 'UP', 'DOWN', 'LEFT' and 'RIGHT' instruction keys to the page
html_element = browser.find_element_by_tag_name('html')

# finally press the instruction keys using selenium
time.sleep(5)
for i in range(50):
	time.sleep(0.5)
	html_element.send_keys(Keys.UP)
	time.sleep(0.5)
	html_element.send_keys(Keys.DOWN)
	time.sleep(0.5)
	html_element.send_keys(Keys.LEFT)
	time.sleep(0.5)
	html_element.send_keys(Keys.RIGHT)

