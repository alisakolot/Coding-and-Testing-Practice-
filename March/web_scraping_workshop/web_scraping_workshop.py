import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)
html = response.content
scraped = BeautifulSoup(html, 'html.parser')

# Get title of first book on the page
# article = scraped.article
first_title = scraped.article.h3.a['title']

# Get titles of books on the page
# scraped.find('article')
articles = scraped.find_all('article')
# articles[0].h3.a['title']
# for article in articles:
#     print(article.h3.a['title'])
    # ^get title for each

#  Get price of all books on the page
# for article in articles:
#     print(float(article.find('p', class_ = 'price_color').text.lstrip('£')))

# Create Dataframe w book title and price of each book on single pg

titles_prices = {}
titles = []
prices = []

for article in articles:
    title = article.h3.a['title']
    price = float(article.find('p', class_ = 'price_color').text.lstrip('£'))
    titles.append(title)
    prices.append(price)
    titles_prices = {'book_titles': titles, 'book_prices':prices}
# print(titles_prices)

# df = pd.DataFrame(titles_prices)
# df.plot()

# Create dataframe with the book title and price for each book across 50 pages
titles_complete = []
prices_complete = []

for n in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{n}.html"
    response = requests.get(url)
    html = response.content
    scraped = BeautifulSoup(html, 'html.parser')
    
    articles = scraped.find_all('articles')

    for article in articles:
        title = article.h3.a['title']
        price = float(article.find('p', class_ = 'price_color').text.lstrip('£'))
        titles_complete.append(title)
        prices_complete.append(price)
        
    
print(titles_complete)
print(prices_complete)
titles_prices_complete = {'book titles':titles_complete, 'book_prices':prices_complete}
    


print('program ran')