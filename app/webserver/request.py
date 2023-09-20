import requests

def categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories1 = r.json()
    one = categories1
    for i in one:
        print(i['name'])