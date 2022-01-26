# -*- coding: utf-8 -*-
'''
Created by Emre MENTESE on 24/01/2022
Coding with Python.
'''

from binance.spot import Spot
from binancema.coininfo import *

KEY         = "XXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXX"

Client = Spot(KEY,SECRET)  # connect binance api

symbol = "OXT"
market = "OXTUSDT"

# TRADE 
print(market_buy_with_price(Client, market, "USDT",30)) # buy 30 $ BTC (market price)

print(market_buy_with_quantity(Client, market,0.01233)) # buy 0.01233 BTC (market price)

# default binance-connector functions
print(f"Server Time: {Client.time()['serverTime']}\n") # get server time

print(f"All Open Orders (LIMIT): {Client.get_open_orders()}\n") #list

print(f"OXT Open Orders (LIMIT): {Client.get_open_orders(market)}\n") #list

print(f"Get only 1 order:{Client.get_order(market,orderId = 55555)} \n") # dict (inpur order id gettin to get_open_orders)

# use libary binancema functions
print(f"Your USDT ($) Balance:                  {balance_usdt(Client)} $\n")              #float

print(f"OXT Quantity (Free):                    {quantity_free(Client,symbol)} OXT\n")     #float

print(f"OXT Quantity (locked):                  {quantity_locked(Client,symbol)} OXT\n")   #float

print(f"OXT Quantity (all):                     {quantity_all(Client,symbol)} OXT\n")      #float

print(f"OXT Balance ($) (free):                 {balance_free(Client,symbol)} $\n")        #float

print(f"OXT Balance ($) (locked):               {balance_locked(Client,symbol)} $\n")      #float

print(f"OXT Balance ($) (all):                  {balance_all(Client,symbol)} $\n")         #float

print(f"OXT/USDT Price (now):                   {price(Client,market)}\n")             #float

print(f"OXT/USDT Price (before 24hr):           {price_before_24hr(Client,market)}\n") #float

print(f"OXT/USDT Price Change Value (24hr):     {price_change24(Client,market)}\n")    #float     

print(f"OXT/USDT Price Change (%) (24hr):       % {price_change_percent24(Client,market)}\n")  #float

print(f"OXT/USDT Price High Value (24hr):       {price_high24(Client,market)}\n")       #float

print(f"OXT/USDT Price Low Value (24hr):        {price_low24(Client,market)}\n")        #float