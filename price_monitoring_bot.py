import requests
from bs4 import BeautifulSoup
import time

def send_message(product_name, product_price):
    message = "Product Found\n" + product_name + '\n' + product_price
    url = "https://api.telegram.org/bot890324614:AAGm5leUftjHfnI6DHFzxHlvHoutFAZSvqc/sendMessage?text={}&chat_id={}".format(message, 689114107)
    requests.get(url)

def check_price():
    url = "https://www.jabong.com/find/kurtas?tt=kurta&rank=0"
    response = requests.get(url)
    print(response)

    soup = BeautifulSoup(response.content, 'html.parser')
    main_body = soup.find('section', class_='row search-product animate-products')
    all_products = main_body.find_all('div', class_='col-xxs-6 col-xs-4 col-sm-4 col-md-3 col-lg-3 product-tile img-responsive')
    for product in all_products:
        product_info = product.find('div', class_='product-info')
        product_name = product_info.find('div', class_='h4')
        product_price = product_info.find('div', class_='price')
        print(product_name.text)
        print(product_price.text)
        try:
            if float(product_price.text) < 1000:
                send_message(product_name.text, product_price.text)
        except:
            print("Cannot Convert to float")

while(True):
    check_price()
    time.sleep(60*60*12)