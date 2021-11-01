# binance-ema
Exchange indicators &amp; Basic functions for Binance API.

- This python library has been written to calculate SMA, EMA, MACD etc. functions with Binance API.
- Complex functions in the Binance API, has been facilitate for developers.

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
# License


    MIT License | Copyright (c) 2021 Emre MENTEŞE

