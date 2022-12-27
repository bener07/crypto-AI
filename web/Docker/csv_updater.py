import sys
sys.path.insert(0, '/com.docker.devenvironments.code/crypto_wallet/')
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_wallet.settings')
django.setup()

from database.models import coins
import requests, threading, time
import pandas as pd

def update(*args, limit=10):
    sym, exc, action = args
    url = f"http://127.0.0.1:5000/{action}"
    data = {
        'sym': sym,
        'exc': exc,
        'limit': limit,
    }
    response = requests.post(url, data=data).json()
    return response




def thread(n):
    import time
    cicle=0
    print(f'Coin {n.coin_name :5}:   running!')
    try:
        os.mkdir(f'../../api/app/csvs/{n.coin_name}')
        open(f'../../api/app/csvs/{n.coin_name}/info.csv', 'w').write('Date, Price\n')
    except FileExistsError:
        pass
    finally:
      while True:
        try:
            cicle += 1
            request = update(n.coin_name, 'eur', 'price')
            date = request.get('time')
            price = request.get('price')
            data = [
            [date, price]
            ]
            coins.objects.filter(coin_name=n.coin_name).update(price=price)
            df = pd.DataFrame(data)
            df.to_csv(f'../../api/app/csvs/{n.coin_name}/info.csv', index=False, mode='a', header=False)
            print(f'Coin {n.coin_name:5} in cicle {cicle:3}    status:   updated!')
        except:
            print(f'Coin {n.coin_name:5} in cicle {cicle:3}    status:   disconnected!\a\7')
            continue
        finally:
            time.sleep(60)


def run_csvs():
    for coin in coins.current_coins():
        th = threading.Thread(target=thread, args=(coin,))
        time.sleep(0.2)
        th.start()



if __name__ == "__main__":
    run_csvs()