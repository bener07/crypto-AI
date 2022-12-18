import unittest
import requests

def requestHandler(action, sym, exc):
    r = requests.post("http://localhost:5000/{}".format(action), data={
        'sym': sym,
        'exc': exc,
        'limit': 10,
    })

class TestLocalAPI(unittest.TestCase):

    def price(self):
        self.assertEqual( requestHandler('price', 'btc', 'eur'), '{\
                "coin": "BTC",\
                "price": 15791.48,\
                "time": "Sat Dec 17 22:27:39 2022"\
                }',
            "Price endpoint not Working")