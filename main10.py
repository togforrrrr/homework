#2
import requests
from bs4 import BeautifulSoup

link = "http://books.toscrape.com"
response = requests.get(link)

soup = BeautifulSoup(response.text, "html.parser")

prices = soup.find_all("p", class_="price_color")

for price in prices:
    print(price.text)
