# binance-ema
Simplified & Professional Binance API.
                      
- Get crypto coin information in an easy way.
- Get account information (balance,quantity etc.)
- Buy / Sell / Limit / Stop Loss --> Orders any way.
- Calculate SMA, EMA, MACD etc. functions (custom indicators)
- https://pypi.org/project/binance-ema/
           
           pip install binance-ema
           
# Nots
- This python library has been written to calculate SMA, EMA, MACD etc. functions with Binance API.
- Complex functions in the Binance API, has been facilitate for developers.
- After installing the libary, don't forget reading the funcions content !
- We are not responsible the your code mistake

# Usage
Firstly, for the use this library you have to create an API via Binance. This documentation will help you for create an safe API.

1) Visit the Binance web site and log in:  https://www.binance.com/
            
2) After, click to your profile photo. Select api management from the menu that appears.

   ![](https://github.com/emrementese/binance-ema/blob/main/examples/images/menu.png)


3) Third, you can create an API now. After the API creatation,  move the API List and click the edit button your API. 

- After the API creatation, save your "API KEY" & "SECRET KEY".
- Page looks like;

   ![](https://github.com/emrementese/binance-ema/blob/main/examples/images/binance-api-settings.png)
   
* Enable Reading was default active. This settings give you authority for reading the coins information. (Red circle in the image)
* Enable Spot-Marign Trading was default passive. !! IF YOU DON'T SPOT-MARGİN TRADİNG, YOU MUST DON'T ACTİVE THİS SETTİNG FOR YOUR SECURİTY. (Green circle in the image)
* Trusted IP default null. You must add your ip adress here for your security. Other ip adress cannot read coins information or trade.
       
> Binance Connector
- This project uses the official binance documentation.
- Github Referance for Binance Connector  -->https://github.com/binance/binance-connector-python
- Original Binance Connector Document     --> https://binance-docs.github.io/apidocs/spot/en/#introduction
- Referance 3 --> https://binance-connector.readthedocs.io/en/stable/
- [Binance Spot Trade Rules](https://www.binance.com/en/trade-rule)
                 
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
## Example Trade Functions
```py

from binance.spot import Spot
from binancema.coininfo import *

KEY         = "XXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXX"

Client = Spot(KEY,SECRET)  # connect binance api

symbol = "OXT"
market = "OXTUSDT"

# TRADE with binance-ema
print(market_buy_with_price(Client, market,30))  # buy 30 $ BTC (market price)

print(market_buy_with_quantity(Client, market,0.01233)) # buy 0.01233 BTC (market price)

# default binance-connector functions
print(f"All Open Orders (LIMIT): {Client.get_open_orders()}\n") #list

print(f"OXT Open Orders (LIMIT): {Client.get_open_orders(market)}\n") #list

print(f"Get only 1 order:{Client.get_order(market,orderId = 55555)} \n") # dict (inpur order id gettin to get_open_orders)
```
# Contributors

<table>
  <tr>
    
   <td align="center"><a href="https://github.com/emrementese"><img src="https://avatars.githubusercontent.com/u/76906642?v=4" width="100px;" alt=""/><br /><sub><b>Emre MENTEŞE (Owner)</b></sub></a><br /></td>

   <td align="center"><a href="https://github.com/ozanmutlu"><img src="https://avatars.githubusercontent.com/u/62659953?v=4" width="100px;" alt=""/><br /><sub><b>Ozan Mutlu</b></sub></a><br /></td>

  </tr>
</table>

# License

    MIT License | Copyright (c) 2022 Emre MENTEŞE

