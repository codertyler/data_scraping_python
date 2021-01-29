from bs4 import BeautifulSoup
import requests
import urllib3

http = urllib3.PoolManager()

cibc_url = "https://www.cibc.com/en/personal-banking/credit-cards/all-credit-cards.html"

response = http.request('GET', cibc_url)
soup = BeautifulSoup(response.data, 'lxml')

for productTitle in soup.find_all('h3', class_="product-title"):
  creditCardName = productTitle.b.text
  print(creditCardName)
