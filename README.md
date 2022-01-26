# binance-ema
Exchange indicators &amp; Basic functions for Binance API.

- https://pypi.org/project/binance-ema/
- This python library has been written to calculate SMA, EMA, MACD etc. functions with Binance API.
- Complex functions in the Binance API, has been facilitate for developers.
- After installing the libary, don't forget reading the funcions content !

# Usage
Firstly, for the use this library you have to create an API via Binance. This documentation will help you for create an safe API.

1) [Visit the Binance web site and log in.](https://www.binance.com/)
            
            https://www.binance.com/
2) After, click to your profile photo. Select api management from the menu that appears.

   ![](https://github.com/emrementese/binance-ema/blob/main/tests/images/menu.png)


3) Third, you can create an API now. After the API creatation,  move the API List and click the edit button your API. 

- After the API creatation, save your "API KEY" & "SECRET KEY".
- Page looks like;

   ![](https://github.com/emrementese/binance-ema/blob/main/tests/images/binance-api-settings.png)
   
* Enable Reading was default active. This settings give you authority for reading the coins information. (Red circle in the image)
* Enable Spot-Marign Trading was default passive. !! IF YOU DON'T SPOT-MARGİN TRADİNG, YOU MUST DON'T ACTİVE THİS SETTİNG FOR YOUR SECURİTY. (Green circle in the image)
* Trusted IP default null. You must add your ip adress here for your security. Other ip adress cannot read coins information or trade.

            You can use this libary now but you need original binance-connector libary for connect to your API.
            
> Binance Connector
- Github Referance for Binance Connector  -->https://github.com/binance/binance-connector-python
- Original Binance Connector Document     --> https://binance-docs.github.io/apidocs/spot/en/#introduction
- Referance 3 --> https://binance-connector.readthedocs.io/en/stable/

                        pip install binance-connector
                        
- You can download and start using and developing the library now.
- Don't forget to sen message me for any mistake. Don't forget give star. I waiting for your pull requests (Forks) :)

## Example connect to API & Info Functions
```py

# Example connect to API & Info Functions

from binance.spot import Spot
from binancema.coininfo import *

KEY         = "XXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXX"

Client = Spot(KEY,SECRET)  # connect binance api

symbol = "OXT"
market = "OXTUSDT"

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

```
## Example Indicator Functions

   coming soon

# License


    MIT License | Copyright (c) 2022 Emre MENTEŞE

