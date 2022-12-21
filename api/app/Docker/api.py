from flask import Flask, request
from CryptoCompareAPI import api
from flask_cors import cross_origin
import time
import logging, sys

app = Flask(__name__)
app.config['CORS_HEADERS'] = ['Content-type, application/json']
app.config['CORS_RESOURCES'] = {r'/*': {"origins": "*"}}
Api = api('8807a578d9a3dd4ad7f132d2f3934d6da75cf68eaf267be1fea2572ef70f92bd')
methods = ['POST']
handler = logging.StreamHandler(sys.stdout)

def getCsvsData(name):
    import csv
    with open(f'/csvs/{name.upper()}/info.csv') as file:
        reader = csv.reader(file)
        data = {'Array': [[i[0],i[1]] for i in reader]}
        return {'Array': data['Array'][1:]}

@app.route('/', methods=methods)
def first_endpoint():
  return "Available urls are: \n/price (requires: 'sym + exc'), \n/top (requires: 'sym + limit'), \n/mining (requires: 'sym + exc'), \n/social (requires: nothing)"


@app.route('/help', methods=methods)
def help():
    return {
        'sym': 'symbol of the coin that you want to get info.', 
        'exc': 'the currency that you want to get, EX: sym=BTC, exc=EUR\n the coin BTC will return it\'s value in euros.',
        'limit': 'the limit of coins when using the /top path.',
        'available urls': 'Available urls are: /price (requires: \'sym + exc\'), /top (requires: \'sym + limit\'), /mining (requires: \'sym + exc\'), /social (requires: nothing)'
    }


@app.route('/csvs/<coin_directory>', methods=methods)
@cross_origin(methods=['POST'])
def csvData(coin_directory):
    return getCsvsData(coin_directory)


@app.route('/price', methods=methods)
def price():
    logging.info("Price accessed!")
    sym = request.form.get('sym')
    exc = request.form.get('exc')
    response = Api.price(sym, exc)
    return {'coin': response[1], 'price': response[2],'time': time.ctime(response[0])}

@app.route('/top', methods=methods)
def top_coins():
    limit = request.form.get('limit')
    sym = request.form.get('sym')
    if limit is None or sym is None :
        return {'error': f'You didn\'t specified limit or symbol!'}
    return {'top': tuple(Api.top(limit, sym))}


@app.route('/historical', methods=methods)
@cross_origin(methods=['POST'])
def history():
    sym = request.form.get('sym').upper()
    exc = request.form.get('exc').upper()
    limit = request.form.get('limit')
    print(sym, exc, limit)
    if limit is None:
        limit = 10
    return {'Array': list(Api.history(sym, exc, limit))}


@app.route('/historytimestamp', methods=methods)
@cross_origin(methods=['POST'])
def historyt():
    sym = request.form.get('sym').upper()
    exc = request.form.get('exc').upper()
    limit = request.form.get('limit')
    print(sym, exc, limit)
    if limit is None:
        limit = 10
    return {'Array': list(Api.historyt(sym, exc, limit))}


@app.route('/mining', methods=methods)
def mining_currency():
    sym, exc = request.form
    return Api.mining_currency(sym,exc)


@app.route('/social', methods=methods)
def social():
    return Api.social()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
