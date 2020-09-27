from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from multiprocessing import Process
from winsound import Beep
from win32api import MessageBox
from time import sleep
import sys

URL = "https://www.maltapost.com/tracking/#/tracking?barcode="
TABLE = (By.CSS_SELECTOR, "table.table-striped")

def setup(url):
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')  # Last I checked this was necessary.
	options.add_experimental_option('excludeSwitches', ['enable-logging'])
	driver = webdriver.Chrome("./chromedriver", options=options)
	driver.get(url)
	return driver

def get_rows(driver):
	# Wait for table to load
	table = WebDriverWait(driver, 15).until(
		EC.visibility_of_element_located(TABLE)
	)

	#print("[DEBUG]", table.get_attribute("outerHTML"))
	return table.find_elements_by_css_selector("tr.ng-scope")

def beep():
	for i in range(10):
		Beep(2500, 250)

def alert(msg, barcode):
	MessageBox(0, msg, barcode, 0x00001030) 

def notify(msg, barcode):
	p_beep = Process(target=beep)
	p_alert = Process(target=alert, args=(msg,barcode,))
	p_beep.start()
	p_alert.start()
	p_beep.join()
	p_alert.join()

def check_for_updates(ignore_rows, barcode):
	Beep(7500, 250) #heartbeat
	driver = setup(URL+barcode)
	rows = get_rows(driver)
	if len(rows) > ignore_rows:
		div = rows[-1].find_element_by_tag_name('div')
		notify(div.text, barcode)

	driver.close()
	return len(rows)

def initialise():
	print("Checks for MaltaPost updates every 5 minutes and lets you know if something changes")
	print("The first alert will show the current state")
	if len(sys.argv) > 1:
		return sys.argv[1]
	else:
		print("Hint: Barcode can be passed as command line argument as well")
		return input('Enter Maltapost barcode : ')

if __name__ == "__main__":
	barcode = initialise()
	ignore_rows = 0
	try:
		while True:
			ignore_rows = check_for_updates(ignore_rows, barcode)
			sleep(300) #check every 5 mins
	except KeyboardInterrupt:
		sys.exit(0)
