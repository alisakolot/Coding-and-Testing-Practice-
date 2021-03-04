import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')


print('program ran')