import requests
from bs4 import BeautifulSoup
import lxml 

def get_link_data(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    name = soup.select_one(selector="#productTitle").getText()
    name = name.strip()

    price = soup.select_one(selector="#priceblock_ourprice").getText()
    price = float(price[1:])

    return name, price


