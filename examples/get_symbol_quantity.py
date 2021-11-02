from binance.spot import Spot as Client
from binancema.indicators import indicator

KEY         = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

connection = Client(KEY,SECRET)  # connect binance api
functions = indicator(connection) #connect the binance-ema libary
troy_info = functions.symbol_quantity("TROY")

troy_quantity_free = troy_info['quantity']
troy_quantity_locked = troy_info['locked']
tyor_balance_usdt = troy_info['balance_usdt']