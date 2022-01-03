import requests
from bs4 import BeautifulSoup

url = 'https://www.toledo24.pro/catalog/ustanovka-vyklyuchateli-rozetki-i-aksessuary/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

data = []

def parse_product():
    print('Парсятся данные с сайта...')
    amount_card_list = soup.find_all('div', {'class': 'product-card js-product-item'})
    group_name = soup.find('h1', {'class': 'sub-title'}).text

    for item in amount_card_list:

            name = (item.findChildren('a', {'itemprop': 'name'}))[0].text
            price = float(((item.findChildren('div', {'class': 'price-current'}))[0].text)[:-3])
            amount_list = (item.findChildren('div', {'class': 'amount-title'}))
            if not amount_list:
                amount = 0

            else: amount = int(((item.findChildren('div', {'class': 'amount-title'}))[0].text)[:-2])

            data.append({
                    'product_name': name,
                    'price': price,
                    'amount': amount,
                    "group_name": group_name
                    })
    print(data)
