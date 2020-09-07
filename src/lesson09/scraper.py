import requests
from bs4 import BeautifulSoup

#Visit Page and parse source HTML
page = requests.get("http://www.python.org")
soup = BeautifulSoup(page.content, 'html.parser')

#Check title is as expected
assert "Python" in soup.title.string

##Perform the search using HTTP GET request
page = requests.get("https://www.python.org/search/?q=pip")
soup = BeautifulSoup(page.content, 'html.parser')

#Look for expected result
link = soup.select_one('a:contains("PEP 439")')

#Get the link URL
print (link['href'])
