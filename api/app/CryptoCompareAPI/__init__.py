import requests
import time

class crypto:
    def __init__(self, api_key):
        self.api_key = api_key

    def top(self, *args):
        limit, sym = args
        url = f'https://min-api.cryptocompare.com/data/top/totaltoptiervolfull?limit={limit}&tsym={sym.upper()}'
        r = requests.get(url).json()
        for i in range(0, int(limit)):
            yield r['Data'][i]['CoinInfo']['Name']
        return



class api(crypto):

    def history(self, sym, exc, limit):
        url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={exc}&tsym={sym}&limit={limit}&api_key={self.api_key}'
        r = requests.get(url).json()
        for i in r.get('Data').get('Data'):
            json = {
                'time': i.get('time'),
                'high': (i.get('high')),
                'low': (i.get('low')),
                'open': (i.get('open')),
                'close': (i.get('close')),
            }
            yield json
        return


    def historyt(self, sym, exc, limit):
        url = f'https://min-api.cryptocompare.com/data/v2/histoday?fsym={exc}&tsym={sym}&limit={limit}&api_key={self.api_key}'
        r = requests.get(url).json()
        for i in r.get('Data').get('Data'):
            json = {
                'time': i.get('time'),
                'high': "{:f}".format(i.get('high')),
                'low': "{:f}".format(i.get('low')),
                'open': "{:f}".format(i.get('open')),
                'close': "{:f}".format(i.get('close')),
            }
            yield json
        return


    def price(self, *args):
        """
        Price function is used to return the price of a certain coin to another kind of real life money
        EX:
            BTC -- USD :is going to return the value of bitcoin in USD dollars.
        :return:
        """
        sym, exc = args
        url = f'https://min-api.cryptocompare.com/data/price?fsym={sym.upper()}&tsyms={exc.upper()}&api_key={self.api_key}'
        r = requests.get(url).json()
        return time.time() ,sym.upper(), r.get(exc.upper())


    def mining_currency(self, *args):
        sym, exc = args
        url = f'https://min-api.cryptocompare.com/data/blockchain/mining/calculator?fsyms={sym.upper()}&tsyms={exc.upper()}&api_key={self.api_key}'
        r = requests.get(url).json()
        return r


    def social(self):
        url = f'https://min-api.cryptocompare.com/data/social/coin/latest?api_key={self.api_key}'
        r = requests.get(url).json()
        return r