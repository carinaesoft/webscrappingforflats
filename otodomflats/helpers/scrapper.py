from bs4 import BeautifulSoup
import httpx

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'.encode(
    'utf-8')

headers = {
    'user-agent': useragent
}

otodomurl = 'https://www.otodom.pl/pl/wyszukiwanie/wynajem/mieszkanie/mazowieckie/warszawa/warszawa/warszawa/wola?page=1&limit=72&market=ALL&ownerTypeSingleSelect=ALL&distanceRadius=0&roomsNumber=%5BTHREE%5D&priceMax=4500&by=DEFAULT&direction=DESC&viewType=listing'

r = httpx.get(otodomurl, headers=headers)
print(r.status_code)

otodomweb = BeautifulSoup(r.text, 'html.parser')
#print(otodomweb.prettify())
offers = []
for promo_offer in otodomweb.find_all('li', {'data-cy': 'listing-item'}):
    print(promo_offer)
    title = promo_offer.find('h3', {'class': 'css-1rhznz4 es62z2j10'}).text
    price = promo_offer.find('span', {'class': 'css-s8wpzb e1brl80i1'}).text
    link = promo_offer.find('a', {'class': 'css-1na6hrw es62z2j13'}, href=True)
    offers.append((title, price, link['href']))





for  flat in offers:
    print(flat)

