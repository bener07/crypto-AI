import sys
sys.path.insert(0, '/com.docker.devenvironments.code/crypto_wallet/')
import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_wallet.settings')
django.setup()

from database.models import coins
import requests, threading, time
import pandas as pd
import logging
import time
from threading import Event

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

class thread(threading.Thread, threading.Event):
    def __init__(self, coin, loggingLevel):
        threading.Thread.__init__(self)
        self.loggingLevel = loggingLevel
        self.event = Event()
        self.name = coin.coin_name # stores the name of the coin
        self.coin = coin # stores the coin object from the database
        self.format = '\033[0;31m%(levelname)s\033[0m:\t %(message)s' # Allows to configure the format of the logging message
    def run(self):
        if self.loggingLevel == 'debug':
            logging.basicConfig(level=logging.DEBUG, format=self.format)
        if self.loggingLevel == 'info':
            logging.basicConfig(level=logging.INFO, format=self.format)
        elif self.loggingLevel == 'warning':
            logging.basicConfig(level=logging.WARNING, format=self.format)
        cicle=0
        logging.info(f'Coin {self.name :5}:   running!') # logging message with the starting message status
        try:
            os.mkdir(f'../../api/app/csvs/{self.name}')
            logging.warning(f'../../api/app/csvs/{self.name}/info.csv', 'w').write('Date, Price\n')
        except FileExistsError:
            pass
        finally:
            while not self.event.is_set():
                try:
                    cicle += 1
                    request = update(self.name, 'eur', 'price')
                    date = request.get('time')
                    price = request.get('price')
                    # writing the data inside a list
                    data = [
                    [date, price]
                    ]
                    coins.objects.filter(coin_name=self.name).update(price=price) #update the price of the coing inside the Database
                    df = pd.DataFrame(data) # create a dataframe
                    df.to_csv(f'../../api/app/csvs/{self.name}/info.csv', index=False, mode='a', header=False) # write the Dataframe inside a CSV
                    logging.info(f'Coin {self.name:5} in cicle {cicle:3}    status:   updated!')
                except:
                    logging.warning(f'Coin {self.name:5} in cicle {cicle:3}    status:   disconnected!\a\7')
                    continue
                finally:
                    time.sleep(60)
            logging.info(f'Coin {self.name:5} in cicle {cicle:3}    status:   Killed!')
    def kill(self):
        self.event.set()
        sys.exit(0)


def run_csvs(self):
    for coin in coins.current_coins():
        th = thread(coin)
        time.sleep(0.1)
        th.start()