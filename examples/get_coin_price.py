from binance.spot import Spot as Client
from binancema.indicators import indicator
from binancema.coininfo import PRICE

KEY         = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

connection = Client(KEY,SECRET)  # connect binance api
functions = indicator(connection) #connect the binance-ema libary

#functions.SMA(series,length)
#functions.EMA(close,length,previous_ema) vb.

btc = PRICE(connection,"BTCUSDT") # use libary coininfo
print(btc)