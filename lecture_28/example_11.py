import os

import requests
from bs4 import BeautifulSoup
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

COINDESK_URL = 'https://www.coindesk.com/price/bitcoin'

API_KEY = os.getenv('SENDGRID_API_KEY')

sg = SendGridAPIClient(API_KEY)


def get_btc_price() -> str:
    response = requests.get(COINDESK_URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    # search by css selector
    spans = soup.select('span[class*="currency-pricestyles"]')
    return spans[1].text


def send_email(btc_price: str, send_to: str = 'lomidzemikheili@gmail.com'):
    message = Mail(
        from_email='mikheil@maxinai.com',
        to_emails=send_to,
        subject='BTC price now',
        html_content=f'მიმდინარე ბიტკოინის ფასია - {btc_price} <br> <br> <br><br><br><br><br>კეთილი სურვილებით, ქართველი ხალხი!')
    response = sg.send(message)
    if response.status_code != 202:
        raise Exception('Email was not sent')


def main():
    btc_price = get_btc_price()
    send_email(btc_price)


if __name__ == "__main__":
    main()
