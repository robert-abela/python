from selenium import webdriver

#Open browser and visit page
driver = webdriver.Chrome()
driver.get("http://www.python.org")

#Check title is as expected
assert "Python" in driver.title

#Find search field
search_field = driver.find_element_by_id("id-search-field")
#Enter search term
search_field.send_keys("pip")
#Find and click the Search button
search_button = driver.find_element_by_id("submit")
search_button.click()

#Look for expected result
link = driver.find_element_by_partial_link_text("PEP 439")
#Get the link URL
print(link.get_attribute("href"))

#Close browser
driver.close()