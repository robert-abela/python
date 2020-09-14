import requests
from bs4 import BeautifulSoup

try:
	page = requests.get("https://www.python.org/search/?q=strings")
except:
	print("Failed to get HTML from the Internet")
else:
	soup = BeautifulSoup(page.content, 'html.parser')
	ul = soup.find('ul', class_="list-recent-events")
	links = ul.find_all('a')
	for link in links:
		print(link.text)
