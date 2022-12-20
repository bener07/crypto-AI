import requests
import unittest

class TestLocalAPI(unittest.TestCase):
    def requestHandler(self, action, sym, exc):
        r = requests.post("http://localhost:5000/{}".format(action), data={
            'sym': sym,
            'exc': exc,
            'limit': 10,
        })
    def test_price(self):
        self.assertEqual( self.requestHandler('price', 'btc', 'eur'), "","Price endpoint not Working")

if __name__ == '__main__':
    unittest.main()