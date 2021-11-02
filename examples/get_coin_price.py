from binance.spot import Spot as Client
from binancema.indicators import indicator

KEY         = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

connection = Client(KEY,SECRET)  # connect binance api
functions = indicator(connection) #connect the binance-ema libary
btc = functions.PRICE("BTCUSDT") # use libary functions
print(btc)