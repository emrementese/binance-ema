from binance.spot import Spot
from binancema.indicators import indicator
from binancema.coininfo import *

KEY         = "XXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXX"

Client = Spot(KEY,SECRET)  # connect binance api
functions = indicator(Client) #connect the binance-ema libary

# default binance-connector

print(f"Server Time: {Client.time()['serverTime']}")
#Client.depth("OXTUSDT", limit=10)

# use libary binancema
print(f"Your USDT ($) Balance:                  {balance_usdt(Client)} $")
print(f"OXT Quantity (Free):                    {quantity_free(Client,'OXT')} OXT")
print(f"OXT Quantity (locked):                  {quantity_locked(Client,'OXT')} OXT")
print(f"OXT Quantity (all):                     {quantity_all(Client,'OXT')} OXT")
print(f"OXT Balance (free):                     {balance_free(Client,'OXT')} $")
print(f"OXT Balance (locked):                   {balance_locked(Client,'OXT')} $")
print(f"OXT Balance (all):                      {balance_all(Client,'OXT')} $")
print(f"OXT/USDT Price (now):                   {price(Client,'OXTUSDT')} $")
print(f"OXT/USDT Price (before 24hr):           {price_before_24hr(Client,'OXTUSDT')} $")
print(f"OXT/USDT Price Change Value (24hr):     {price_change24(Client,'OXTUSDT')} $")
print(f"OXT/USDT Price Change (%) (24hr):       % {price_change_percent24(Client,'OXTUSDT')}") 
print(f"OXT/USDT Price High Value (24hr):       {price_high24(Client,'OXTUSDT')} $") 
print(f"OXT/USDT Price Low Value (24hr):        {price_low24(Client,'OXTUSDT')} $")