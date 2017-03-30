import copy
import json
import os
import requests
import selenium
import sys
import time
from subprocess import call
from selenium import webdriver

#display = Display(visible=0, size=(1024,768))
#display.start()

browser = webdriver.Chrome()
browser.get("https://darksky.net/forecast/35.0456,-85.3097/us12/en")

current_temp = browser.find_element_by_class_name("currently").text
current_temp = current_temp.encode('utf-8')

forecast = browser.find_element_by_css_selector(".next.swap").text
forecast = forecast.encode('utf-8')

mintemp = browser.find_element_by_class_name("minTemp").text
maxtemp = browser.find_element_by_class_name("maxTemp").text

temp_summary = "The high today is %s while the low today is %s" % (maxtemp, mintemp)
temp_summary = temp_summary.encode('utf-8')

digest_template = open("digest.txt", "w")
digest_template.write(current_temp + "\n")
digest_template.write(forecast + "\n")
digest_template.write(temp_summary + "\n\n\n")

browser.get("https://www.nytimes.com/column/learning-word-of-the-day")

word_story = browser.find_element_by_css_selector(".story.theme-summary.no-thumb")
word_story.click()
word = browser.find_element_by_css_selector(".story-subheading.story-content").text
word= word.encode('utf-8')
definition = browser.find_element_by_css_selector(".story-quote.story-content").text
definition = definition.encode('utf-8')

digest_template.write("Word Of The Day!\n\n" + word + "\n" + definition + "\n\n")
digest_template.close()
browser.quit()

call(["./sendmail.sh"])
