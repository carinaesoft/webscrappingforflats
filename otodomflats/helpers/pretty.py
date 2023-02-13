import requests
from bs4 import BeautifulSoup
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'.encode('utf-8')

headers = {
    'user-agent': useragent
}
otodom_url = 'https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/warszawa/wola?market=ALL&ownerTypeSingleSelect=ALL' \
            '&distanceRadius=0&roomsNumber=%5BTHREE%5D&locations=%5Bdistricts_6-117%5D&priceMax=4500&by=DEFAULT' \
            '&direction=DESC&viewType=listing '

response = requests.get(otodom_url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())
