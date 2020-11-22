from selenium import webdriver
import time

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/alert_accept.html")

	button = browser.find_element_by_css_selector("button.btn")
	button.click()

	confirm = browser.switch_to.alert
	confirm.accept()

	import math
	def calc(x):
	 	 return str(math.log(abs(12*math.sin(int(x)))))

	span1 = browser.find_element_by_id("input_value")
	span1_input_value = span1.text
	x = span1.text
	y = calc(x)

	input = browser.find_element_by_id("answer") 
	input.send_keys(y)
	button = browser.find_element_by_css_selector("button.btn")	
	button.click()
	
finally:
	time.sleep(20)
	browser.quit()

		