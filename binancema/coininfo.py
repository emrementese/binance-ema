'''
Created by Emre MENTESE on 24/01/2022
Coding with Python.
'''

def symbol_quantity(client,symbol) -> dict:
        '''
        * Get your coins quantitiy or balance.

        - Input
            * Coin symbol: BTC , DENT , ETH , TROY

        - Outputs
            * locked  --> coins quantity in order
            * balance -->  free coins quantity * price usd  (no locked)
        '''
        if symbol == "USDT":
            raise Exception("Symbol Error: Use balance_usdt function.")

        hesap = client.account()
        for coin in hesap['balances']:
            if coin['asset'] == symbol:
                fiyat = float(client.ticker_price(symbol + "USDT")['price'])
                bakiye =  float(coin['free']) * fiyat
                return {"symbol":symbol, "quantity": float(coin['free']),"locked":float(coin['locked']),"balance_usdt":bakiye}
            else:
                continue

def balance_usdt(client) -> float:
        '''
        * Get your account balance USDT ($)
        '''
        hesap = client.account()
        for coin in hesap['balances']:
            if coin['asset'] == 'USDT':
                return float(coin['free'])
            else:
                continue

def price(client,symbol) -> float:
        '''
        * This function return the instant price the symbol.

        - Example:  BTCUSDT -> 62000 ($) Float
        '''
        data = client.ticker_price(symbol)
        return float(data['price'])