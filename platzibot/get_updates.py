import requests
import time

def get_update(token, offset = None):
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    params = {'offset':offset} if offset else{}
    response = requests.get(url,params=params)
    return response.json()

def print_new(token):
    offset = None
    while True:
        updates = get_update(token,offset)
        if 'result' in updates:
            for update in updates['result']:
                message = update['message']
                id = message['from']['id']
                username = message["from"]["first_name"]
                text = message.get('text')
                print(f'Usuario: {username} {id}')
                print(f'mensaje:{text}')
                print('---')
                offset = update['update_id'] + 1
        time.sleep(1)

token = '6144759486:AAFiWBIUYdi4SR8fFhcdiLO1sFZSiZ9Kvbo'
print_new(token)