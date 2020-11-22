from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	browser = webdriver.Chrome()
	browser.get("http://suninjuly.github.io/explicit_wait2.html")	

	button =browser.find_element(By.ID, "book")
	button_book = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "100")
		)
	button.click()

	import math

	def calc(x):
	 	 return str(math.log(abs(12*math.sin(int(x)))))

	span1 = browser.find_element(By.ID, "input_value")
	span1_input_value = span1.text
	x = span1.text
	y = calc(x)

	input = browser.find_element(By.ID, "answer") 
	input.send_keys(y)
	button = browser.find_element(By.ID, "solve")	
	button.click()
finally:
	time.sleep(20)
	browser.quit()

