# Retrieve the current bitcoin price in USD using requests and beautifulsoup4

import requests
from bs4 import BeautifulSoup

url = 'https://www.coindesk.com/price/bitcoin'
while True:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # search by css selector
    spans = soup.select('span[class*="currency-pricestyles"]')
    print(f'The current price of Bitcoin is: {spans[1].text}')
