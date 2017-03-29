import requests
import selenium
import time
import sys
import copy
import os
import json
from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from pyvirtualdisplay import display

#display = Display(visible=0, size=(1024,768))
#display.start()

browser = webdriver.Chrome()
browser.get("https://darksky.net/forecast/35.0456,-85.3097/us12/en")

current_temp = browser.find_element_by_class_name("temp swip")
current_status = browser.find_element_by_class_name("summary swap")