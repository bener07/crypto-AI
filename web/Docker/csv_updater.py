import sys
sys.path.insert(0, '/com.docker.devenvironments.code/crypto_wallet/')
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_wallet.settings')
django.setup()

from database.models import coins
import requests, threading, time
import pandas as pd
import logging

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


class thread(threading.Thread):
    def __init__(self, name, loggingLevel):
        self.loggingLevel = loggingLevel
        self.k = False
        self.name = name
        self.format = '\033[0;31m%(levelname)s\033[0m:\t %(message)s'


class csvs:
    def kill(self):
        self.k = True
    def thread(self, n):
        if self.loggingLevel == 'debug':
            logging.basicConfig(level=logging.DEBUG, format=self.format)
        if self.loggingLevel == 'info':
            logging.basicConfig(level=logging.INFO, format=self.format)
        elif self.loggingLevel == 'warning':
            logging.basicConfig(level=logging.WARNING, format=self.format)
        import time
        cicle=0
        logging.info(f'Coin {n.coin_name :5}:   running!')
        self.k = False
        try:
            os.mkdir(f'../../api/app/csvs/{n.coin_name}')
            logging.warning(f'../../api/app/csvs/{n.coin_name}/info.csv', 'w').write('Date, Price\n')
        except FileExistsError:
            pass
        finally:
            while not self.k:
                try:
                    cicle += 1
                    request = update(n.coin_name, 'eur', 'price')
                    date = request.get('time')
                    price = request.get('price')
                    # writing the data inside a list
                    data = [
                    [date, price]
                    ]
                    coins.objects.filter(coin_name=n.coin_name).update(price=price) #update the price of the coing inside the Database
                    df = pd.DataFrame(data) # create a dataframe
                    df.to_csv(f'../../api/app/csvs/{n.coin_name}/info.csv', index=False, mode='a', header=False) # write the Dataframe inside a CSV
                    logging.info(f'Coin {n.coin_name:5} in cicle {cicle:3}    status:   updated!')
                except:
                    logging.warning(f'Coin {n.coin_name:5} in cicle {cicle:3}    status:   disconnected!\a\7')
                    continue
                finally:
                    time.sleep(60)
            logging.info(f'Coin {n.coin_name:5} in cicle {cicle:3}    status:   Killed!')
    def run_csvs(self):
        for coin in coins.current_coins():
            th = threading.Thread(target=self.thread, args=(coin,))
            time.sleep(0.1)
            th.start()