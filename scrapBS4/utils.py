import requests
from bs4 import BeautifulSoup
import lxml
from requests.models import Response 

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

def get_dict_data(word):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
    }
    search = word
    url = 'https://www.dictionary.com/browse/'+word
    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")
    meaning = soup.find('span',{'class':'one-click-content css-nnyc96 e1q3nk1v1'}).getText()

    return search, meaning
   
def get_link_meta(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Accept-Language":"en-GB,en-US;q=0.9,en;q=0.8"
    }

    metares = requests.get(url, headers=headers)
    soup = BeautifulSoup(metares.text, "lxml")
    title = soup.find('title').getText()
    metas = soup.find_all('meta')
    description = [ meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'description' ]
    keywords = [meta.attrs['content'] for meta in metas if 'name' in meta.attrs and meta.attrs['name'] == 'keywords']
  
    return title, description, keywords


url = 'https://www.sigmasoftwares.org/'
print(get_link_meta(url))
