#! python3

# commandlineemailer.py - send messages from a Facebook or Twitter account
# usage commandline instruction [filename] [login ID] [Login Password] [recipient Name] [message]

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, time

# save the command line input to respective variables
if len(sys.argv) > 1:
	loginId_input = sys.argv[1]
	loginPass_input = sys.argv[2]
	send_to_user = sys.argv[3]
	message = sys.argv[4:]

# xpath information for easy edit
search_element_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input'
matched_element_xpath = '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div[1]/ul/li[1]/ul/li/div/a/div'

# selenium webdriver to open firefox browser
browser = webdriver.Firefox()
browser.get('http://facebook.com/messages')

# login credentials
loginId_element = browser.find_element_by_id('email')
loginId_element.send_keys(loginId_input)

loginPass_element = browser.find_element_by_id('pass')
loginPass_element.send_keys(loginPass_input)
loginPass_element.send_keys(Keys.ENTER)

# message the user
time.sleep(10)
search_userElement = browser.find_element_by_xpath(search_element_xpath)
search_userElement.send_keys(send_to_user)

time.sleep(3)
matched_contactElement = browser.find_element_by_xpath(matched_element_xpath)
matched_contactElement.click()

time.sleep(3)
message_boxElement = browser.find_element_by_css_selector('.notranslate')
message_boxElement.send_keys(message)
message_boxElement.send_keys(Keys.ENTER)
