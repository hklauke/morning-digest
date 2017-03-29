import copy
import json
import os
import requests
import selenium
import sys
import time
#from pyvirtualdisplay import display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


import yagmail
yag = yagmail.SMTP()

#display = Display(visible=0, size=(1024,768))
#display.start()

browser = webdriver.Chrome()
browser.get("https://darksky.net/forecast/35.0456,-85.3097/us12/en")

current_temp = browser.find_element_by_class_name("currently").text
print(current_temp)

forecast = browser.find_element_by_css_selector(".next.swap").text
print(forecast)

mintemp = browser.find_element_by_class_name("minTemp").text
maxtemp = browser.find_element_by_class_name("maxTemp").text

temp_summary = "The high today is %s while the low today is %s", maxtemp, mintemp
print(temp_summary)

contents = [current_temp, forecast. temp_summary]
yag.send('klauke9@gmail.com', 'Waking Up Is Hard!', contents)
