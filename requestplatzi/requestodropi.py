import requests

def scraping():
    x = requests.get('https://app.rocketfy.co/pedidos/en-transito/646d4c92e987cd3cdf6344fd?order_father_id=646d4c92e987cd3cdf6344fb')
    print(x.status_code)
    print(x.text)


if __name__ == '__main__':
    scraping()