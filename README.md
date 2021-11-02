# binance-ema
Exchange indicators &amp; Basic functions for Binance API.

- This python library has been written to calculate SMA, EMA, MACD etc. functions with Binance API.
- Complex functions in the Binance API, has been facilitate for developers.
- After installing the libary, don't forget reading the funcions content !

# Usage
Firstly, for the use this library you have to create an API via Binance. This documentation will help you for create an safe API.

1) [Visit the Binance web site and log in.](https://www.binance.com/)
            
            https://www.binance.com/
2) After, click to your profile photo. Select api management from the menu that appears.

   ![](https://github.com/emrementese/binance-ema/blob/main/examples/images/menu.png)


3) Third, you can create an API now. After the API creatation,  move the API List and click the edit button your API. 

- After the API creatation, save your "API KEY" & "SECRET KEY".
- Page looks like;

   ![](https://github.com/emrementese/binance-ema/blob/main/examples/images/binance-api-settings.png)
   
* Enable Reading was default active. This settings give you authority for reading the coins information. (Red circle in the image)
* Enable Spot-Marign Trading was default passive. !! IF YOU DON'T SPOT-MARGİN TRADİNG, YOU MUST DON'T ACTİVE THİS SETTİNG FOR YOUR SECURİTY. (Green circle in the image)
* Trusted IP default null. You must add your ip adress here for your security. Other ip adress cannot read coins information or trade.

            You can use this libary now but you need original binance-connector libary for connect to your API.
            
> Binance Connector
- Github Referance for Binance Connector  -->https://github.com/binance/binance-connector-python
- Original Binance Connector Document     --> https://binance-docs.github.io/apidocs/spot/en/#introduction
- Referance 3 --> https://binance-connector.readthedocs.io/en/stable/

                        pip install binance-connector
                        
- You can now download and start using and developing the library.
- Don't forget to sen message me for any mistake. Don't forget give star. I waiting for your pull requests (Forks) :)

## Examples
```py

# example connect to API

from binance.spot import Spot as Client

KEY         = "XXXXXXXXXXXXXXXXXXXXXXXXXX"
SECRET      = "XXXXXXXXXXXXXXXXXXXXXXXXXX"

connection = Client(KEY,SECRET)  # connect binance api
functions = indicator(connection) #connect the binance-ema libary
btc = functions.PRICE("BTCUSDT") # use libary functions
print(btc)

```

# License


    MIT License | Copyright (c) 2021 Emre MENTEŞE

