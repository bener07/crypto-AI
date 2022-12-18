import unittest


class TestLocalAPI(unittest.TestCase):
    def requestHandler(action, sym, exc):
        import requests
        r = requests.post("http://localhost:5000/{}".format(action), data={
            'sym': sym,
            'exc': exc,
            'limit': 10,
        })
    def price(self):
        self.assertEqual( self.requestHandler('price', 'btc', 'eur'), '{\
                "coin": "BTC",\
                "price": 15791.48,\
                "time": "Sat Dec 17 22:27:39 2022"\
                }',
            "Price endpoint not Working")