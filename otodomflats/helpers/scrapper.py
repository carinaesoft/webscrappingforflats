from bs4 import BeautifulSoup
import httpx

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'.encode('utf-8')

headers = {
    'user-agent': useragent
}

otodomurl = 'https://www.otodom.pl/pl/oferty/wynajem/mieszkanie/warszawa/wola?market=ALL&ownerTypeSingleSelect=ALL' \
            '&distanceRadius=0&roomsNumber=%5BTHREE%5D&locations=%5Bdistricts_6-117%5D&priceMax=4500&by=DEFAULT' \
            '&direction=DESC&viewType=listing '

r = httpx.get(otodomurl, headers=headers)


test

otodomweb = BeautifulSoup(r.text, 'html.parser')



for offer in otodomweb.select("listing-item"):
    title = offer.select_one("h3")

    print(title)