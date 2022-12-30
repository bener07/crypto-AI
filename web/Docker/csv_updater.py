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

API_PATH = '../../api/app/csvs/'

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
        self.config = {
            'format': '\033[0;31m%(levelname)s\033[0m:\t %(message)s',
            'status': 'Not initiated',
            'kill': False,
        }

    def kill(self):
        global killed
        killed = True
        return 0

    def sleep(self, secs):
        # self.config['kill'] = False
        counter = 0
        global killed
        while counter < secs:
            if killed:
                break
            else:
                counter += 1
                time.sleep(1)
        return 0

    def run(self):
        if self.loggingLevel == 'debug':
            logging.basicConfig(level=logging.DEBUG, format=self.config['format'])
        if self.loggingLevel == 'info':
            logging.basicConfig(level=logging.INFO, format=self.config['format'])
        elif self.loggingLevel == 'warning':
            logging.basicConfig(level=logging.WARNING, format=self.config['format'])
        cicle=0
        global killed
        killed = False
        logging.info(f'Coin {self.name :5}:   running!') # logging message with the starting message status
        try:
            os.mkdir(API_PATH+f'{self.name}')
            open(API_PATH+f'{self.name}/info.csv', 'w').write('Date, Price\n')
        except FileExistsError:
            pass
        finally:
            while not killed:
                try:
                    cicle += 1
                    request = update(self.name, 'eur', 'price')
                    date = request.get('time')
                    price = request.get('price')
                    self.config['status'] = "Running"
                    # writing the data inside a list
                    data = [
                    [date, price]
                    ]
                    coins.objects.filter(coin_name=self.name).update(price=price) #update the price of the coing inside the Database
                    df = pd.DataFrame(data) # create a dataframe
                    df.to_csv(API_PATH+f'{self.name}/info.csv', index=False, mode='a', header=False) # write the Dataframe inside a CSV
                    logging.info(f'Coin {self.name:5} in cicle {cicle:3}    status:   updated!')
                except:
                    logging.warning(f'Coin {self.name:5} in cicle {cicle:3}    status:   disconnected!\a\7')
                    self.config['status'] = "Disconnected, check the api or Internet connection"
                    continue
                finally:
                        self.sleep(60)
                if killed:
                    logging.warning(f'Coin {self.name:5}    status:   Killed!')