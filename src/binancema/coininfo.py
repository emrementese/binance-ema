# -*- coding: utf-8 -*-
"""
Created by Emre MENTESE on 24/01/2022
Coding with Python.
"""

import math
from typing import Union


def decorator_quantity(func):
    def inner(client, symbol):
        Account = client.account()
        for coin in Account["balances"]:
            if coin["asset"] != symbol:
                continue
            return func(client, symbol, coin=coin)

    return inner


def round_stepsize(value: Union[int, float], step_size: Union[int, float]) -> float:
    """
    * Round value to step_size for Trade Rules.
    """
    precision: int = int(round(-math.log(step_size, 10), 0))
    return float(round(value, precision))


@decorator_quantity
def quantity_free(client, symbol: str, coin=None) -> float:
    """
    * Get your coins free quantitiy.

    - Input
        * Coin symbol: BTC , DENT , ETH , TROY

    - Outputs
        * Free quantitiy -> Float
    """
    return float(coin["free"])


@decorator_quantity
def quantity_locked(client, symbol: str, coin=None) -> float:
    """
    * Get your coins locked quantitiy.

    - Input
        * Coin symbol: BTC , DENT , ETH , TROY

    - Outputs
        * Locked quantitiy -> Float
    """
    return float(coin["locked"])


@decorator_quantity
def quantity_all(client, symbol: str, coin=None) -> float:
    """
    * Get your coins all (locked + free) quantitiy.

    - Input
        * Coin symbol: BTC , DENT , ETH , TROY

    - Outputs
        * all quantitiy -> Float
    """
    return float(coin["locked"]) + float(coin["free"])


@decorator_quantity
def balance_free(client, symbol: str, coin=None) -> float:
    """
    * Get your coins free balance $ (Instant Price USDT).

    - Input
        * Coin symbol: BTC , DENT , ETH , TROY

    - Outputs
        * free balance -> Float
    """
    ticker_price = float(client.ticker_price(symbol + "USDT")["price"])
    balance = float(coin["free"]) * ticker_price
    return balance


@decorator_quantity
def balance_locked(client, symbol: str, coin=None) -> float:
    """
    * Get your coins locked balance $ (Instant Price USDT).

    - Input
        * Coin symbol: BTC , DENT , ETH , TROY

    - Outputs
        * locked balance -> Float
    """
    ticker_price = float(client.ticker_price(symbol + "USDT")["price"])
    balance = float(coin["locked"]) * ticker_price
    return balance


@decorator_quantity
def balance_all(client, symbol: str, coin=None) -> float:
    """
    * Get your coins all (locked + free) balance $ (Instant Price USDT).

    - Input
        * Coin symbol: BTC , DENT , ETH , TROY

    - Outputs
        * all balance -> Float
    """
    ticker_price = float(client.ticker_price(symbol + "USDT")["price"])
    balance = (float(coin["locked"]) + float(coin["free"])) * ticker_price
    return balance


def balance_usdt(client) -> float:
    """
    * Get your account balance USDT (Instant Price USDT $)
    """
    hesap = client.account()
    for coin in hesap["balances"]:
        if coin["asset"] != "USDT":
            continue
        return float(coin["free"])


def price(client, symbol: str) -> float:
    """
    * This function return the instant price value the symbol.

    - Input
        * Coin market: BTCUSDT

    - Outputs
        * instant price value  -> Float
    """
    return float(client.ticker_price(symbol)["price"])


def price_before_24hr(client, symbol: str) -> float:
    """
    * This function return the before 24hr price value the symbol.

    - Input
    * Coin market: BTCUSDT

    - Outputs
    * before 24hr price -> Float
    """
    return float(client.ticker_24hr(symbol)["openPrice"])


def price_change24(client, symbol: str) -> float:
    """
    * Get 24hr Ticker Price Change value

    - Input
        * Coin market: BTCUSDT

    - Outputs
        * 24hr price change -> Float
    """
    return float(client.ticker_24hr(symbol)["priceChange"])


def price_high24(client, symbol: str) -> float:
    """
    * Get 24hr Ticker Price High value

    - Input
        * Coin market: BTCUSDT

    - Outputs
        * 24hr High price -> Float
    """
    return float(client.ticker_24hr(symbol)["highPrice"])


def price_low24(client, symbol: str) -> float:
    """
    * Get 24hr Ticker Price Low value

    - Input
        * Coin market: BTCUSDT

    - Outputs
        * 24hr Low price -> Float
    """
    return float(client.ticker_24hr(symbol)["lowPrice"])


def price_change_percent24(client, symbol: str) -> float:
    """
    * Get 24hr Ticker Price Change Percent (%)

    - Input
        * Coin market: BTCUSDT

    - Outputs
        * 24hr Price Change Percent -> Float
    """
    return float(client.ticker_24hr(symbol)["priceChangePercent"])


def price_average(client, symbol: str) -> float:
    """
    * Get Average Price value

    - Input
        * Coin market: BTCUSDT

    - Outputs
        * 24hr Price Change Percent -> Float
    """
    return float(client.avg_price(symbol)["price"])


def candlesticks(client, symbol: str, time, count) -> list:
    """
    * Get candlestick data for the given symbol graph.

    - time : 1m, 15m 1h , 4h , 1d , 1w ...
    """
    return client.klines(symbol, time, count)


def market_buy_with_price(
    client, symbol: str, price: Union[int, float]
) -> Union[bool, dict]:
    """
    * New order to buy coin with MARKET price (Use to price).

    For Example: BTCUSDT -> market_buy_with_price(client,BTCUSDT,USDT,150) You will get $150 BTC

    - Input
        * symbol --> BTCUSDT , BTCBNB, BTCETH... (str)
        * price -->  560 $ , 0.323 BNB, 22 ETH... (float)

    - Outputs
        * if success to order return order info dict
        {'buy_price': '372.90000000', 'qty': '0.00100000', 'comission': '0.00000075'}
        * else fail to order return False
    """
    try:
        # TRADE RULES CONTROL

        # 1- Input Type control
        if not isinstance(symbol, str):
            raise Exception("Type Error: symbol must be str (BTCUSDT etc.).")

        if not isinstance(price, (int, float)):
            raise Exception("Type Error: Price must be float or int.")

        r = client.exchange_info(symbol)
        quoteAsset = r["symbols"][0]["quoteAsset"]

        # 2- PRICE_FILTER Control
        minPrice = float(r["symbols"][0]["filters"][0]["minPrice"])
        maxPrice = float(r["symbols"][0]["filters"][0]["maxPrice"])
        tickSize = float(r["symbols"][0]["filters"][0]["tickSize"])
        validated_price = round_stepsize(price, tickSize)

        if (validated_price < minPrice) or (validated_price > maxPrice):
            raise Exception(
                f"PRICE_FILTER Error: Price is not in range Min: {minPrice} - Max: {maxPrice}"
            )

        # 3- MIN_NOTIONAL Control
        minNotional = float(r["symbols"][0]["filters"][3]["minNotional"])
        if validated_price < minNotional:
            raise Exception(
                f"MIN_NOTIONAL Error: Minimum Trade Amount: {minNotional} {quoteAsset}"
            )

        # 4- Balance Control
        balance = quantity_free(client, quoteAsset)
        if balance < validated_price:
            raise Exception(
                f"Balance Error: You don't have enough balance to buy this coin ({quoteAsset}:{balance})"
            )

        params = {
            "symbol": symbol,
            "side": "BUY",
            "type": "MARKET",
            "quoteOrderQty": str(validated_price),
        }
        response = client.new_order(**params)
        return {
            "buy_price": response["fills"][0]["price"],
            "qty": response["fills"][0]["qty"],
            "comission": response["fills"][0]["commission"],
        }

    except Exception as e:
        print(e)
        return False


def market_buy_with_quantity(
    client, symbol: str, quantity: Union[int, float]
) -> Union[bool, dict]:
    """
    * New order to buy coin with MARKET price (Use to quantity).

    For Example: BTCUSDT -> market_buy_with_price(client,BTCUSDT,USDT,0.01234) You will get 0.01234 BTC

    - Input
        * symbol --> BTCUSDT , BTCBNB, BTCETH...
        * symbol --> USDT , BNB , ETH...
        * quantity -->  560 , 0.323, 22...

    - Outputs
        * if success to order return order info dict
        {'buy_price': '372.90000000', 'qty': '0.00100000', 'comission': '0.00000075'}
    """

    try:
        # TRADE RULES CONTROL

        # 1- Input type control
        if not isinstance(symbol, str):
            raise Exception("Type Error: symbol must be str (BTCUSDT etc.).")

        if not isinstance(quantity, (int, float)):
            raise Exception("Quantity Error: Quantity must be float or int.")

        r = client.exchange_info(symbol)
        quoteAsset = r["symbols"][0]["quoteAsset"]

        # 2- LOT_SIZE Control

        # Market Lot Size
        minQty = float(r["symbols"][0]["filters"][5]["minQty"])
        maxQty = float(r["symbols"][0]["filters"][5]["maxQty"])
        stepSize = float(r["symbols"][0]["filters"][5]["stepSize"])

        #  if not has got marektlosize , use to Order Lot Size
        if minQty == 0:
            minQty = float(r["symbols"][0]["filters"][2]["minQty"])
        if maxQty == 0:
            maxQty = float(r["symbols"][0]["filters"][2]["maxQty"])
        if stepSize == 0:
            stepSize = float(r["symbols"][0]["filters"][2]["stepSize"])

        validated_quantity = round_stepsize(quantity, stepSize)

        if (validated_quantity < minQty) or (validated_quantity > maxQty):
            raise Exception(
                f"LOT_SIZE Error: Quantity is not in range Min: {minQty} - Max: {maxQty}"
            )

        # 3- MIN_NOTIONAL Control
        minNotional = float(r["symbols"][0]["filters"][3]["minNotional"])

        price_now = price_average(client, symbol)
        balance = price_now * validated_quantity

        if balance < minNotional:
            raise Exception(
                f"MIN_NOTIONAL Error: Minimum Trade Amount: {minNotional} {quoteAsset}"
            )

        # 4- Balance Control
        balance_control = quantity_free(client, quoteAsset)

        if balance > balance_control:
            raise Exception(
                f"Balance Error: You don't have enough balance to buy this coin ({quoteAsset}:{balance_control})"
            )

        params = {
            "symbol": symbol,
            "side": "BUY",
            "type": "MARKET",
            "quantity": str(quantity),
        }
        response = client.new_order(**params)
        return {
            "buy_price": response["fills"][0]["price"],
            "qty": response["fills"][0]["qty"],
            "comission": response["fills"][0]["commission"],
        }
    except Exception as e:
        print(e)
        return False
