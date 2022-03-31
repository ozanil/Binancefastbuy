from binance import Client,exceptions,helpers
import configparser
import threading

def buy_order(api_key,api_secret,symbol,quantity):
    print('Buying '+str(quantity)+' '+symbol)
    try:
        client = Client(api_key, api_secret)
        client.order_market_buy(symbol=symbol,quoteOrderQty=quantity)
    except exceptions.BinanceAPIException as e:
        print(e)
        buy_order(api_key, api_secret, symbol, quantity)
    except exceptions.BinanceOrderException as e:
        print(e)
        buy_order(api_key,api_secret,symbol,quantity)


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    api_key = config.get('APISETTINGS','api_key')
    api_secret = config.get('APISETTINGS','api_secret')
    symbol = config.get('APISETTINGS','symbol')
    quantity = config.get('APISETTINGS','quantity')
    # start thread x 10
    for i in range(10):
        threading.Thread(target=buy_order,args=(api_key,api_secret,symbol,quantity)).start()

