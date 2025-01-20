# -*- coding: utf-8 -*-
"""
Created by Emre MENTESE on 24/01/2022
Coding with Python.
"""
from binancema.coininfo import price


class indicator:

    def __init__(self, client):
        self.client = client

    def SMA(self, series, length) -> float:
        """
        * Simple Moving Average
        * Referance (01/11/2021): https://www.tradingview.com/pine-script-reference/#fun_sma
        * If you want look at the original SMA function coded with Pine Script, visit the reference.

        - length --> Data count len(series) (int)
        - series --> data (list) or (int- float)
        """
        if isinstance(length, int):
            pass
        else:
            raise Exception("SMA Calculating Error: Length must be integer.")

        if isinstance(series, list):
            sum = 0
            for i in series:
                if isinstance(i, (int, float)):
                    sum += i
                else:
                    raise Exception(
                        "SMA Calculating Error: series elements must be integer or float."
                    )
            return sum

        elif isinstance(series, (float, int)):
            return series / length

        else:
            raise Exception(
                "SMA Calculating Error: series must be integer & float or list."
            )

    def EMA(self, close, length, previous_ema) -> float:
        """
        * Exponential Moving Avarage
        * Referance (01/11/2021): https://www.tradingview.com/pine-script-reference/#fun_ema
        * If you want look at the original EMA function coded with Pine Script, visit the reference.

            Firstly Binance not give EMA information for cripto coins. If you want calculate to last EMA, you must use
        previous EMA. You can't take a previous EMA with Binance. You must calculate. You need previous to previous EMA
        to calculate previous EMA. This goes as far as the first EMA. If you want calculate to the first EMA, you must
        use SMA in the EMA calculate. However, calculating first EMA using SMA is inconvenient and takes too long and
        Binance has an api limit. Binance max give to the 1000 candlestick bars. You can't calculate SMA with this candlestick bars.

        * For example: You can't calculate BTC-USDT  5 minute grahpic's EMA. Because you need more candlestick bars information (Billion)
        * That's Why we can add one more input in the function. (previous_EMA)
        * This input can be any EMA provided it is an EMA before the EMA of the last candlestick bars.

        length : Number of candlestick bars (Integer)
        previous_ema : can be any EMA provided it is an EMA before the EMA of the last candlestick bars. (Float-Integer)
        close  : The closing value of the candlestick bars after the previous EMA candlestick bar (Float-Integer)

        return --> next EMA

        """
        if isinstance(length, int):
            pass
        else:
            raise Exception("EMA Calculating Error: Length must be integer.")

        if isinstance(previous_ema, (float, int)):
            pass
        else:
            raise Exception(
                "EMA Calculating Error: previous_ema must be integer or float."
            )

        if isinstance(close, (float, int)):
            pass
        else:
            raise Exception("EMA Calculating Error: close must be integer or float.")

        alpha = 2 / (length + 1)
        ema = (close * alpha) + (previous_ema * (1 - alpha))
        return ema

    def coins_instant_ema(self, length, previous_ema, symbol) -> float:
        """
        * This function return instant ema using with the ema of the previous candlestick bars

        Note:
            * When the graphic move to a next candlestick bars you have to change the ema and run it again !
            * This function can't calculating next candlestick bars's ema. İt can just return instant (dynamic) ema !

        Examples
        - symbol = "BTCUSDT"
        - length = 9
        - previous_ema (9) = 62017.40

        """

        close_value = price(self.client, symbol)
        return self.EMA(close_value, length, previous_ema)

    def MACD(
        self,
        close,
        fast,
        slow,
        signal,
        previous_ema_fast,
        previous_ema_slow,
        previous_macd,
    ):
        """
        * Moving Average Convergence Divergence
        * Referance (01/11/2021): https://en.tradingview.com/ideas/macd/
        * If you want look at the original MACD function coded with Pine Script, visit the reference.


        - close  --> The closing value of the candlestick bars after the previous EMA candlestick bar (Float-Integer)
        - fast   --> fast ema length
        - slow   --> slow ema length
        - signal --> signal length

        - previous_ema_fast --> can be any ema provided it is an ema before the ema of the last candlestick bars. (Float-Integer)
        - previous_ema_slow --> can be any ema provided it is an ema before the ema of the last candlestick bars. (Float-Integer)
        - previous_macd     --> can be any macd provided it is an macd before the macd of the last candlestick bars. (Float-Integer)

        """
        fastMA = self.EMA(close, fast, previous_ema_fast)  # next fast ema
        slowMA = self.EMA(close, slow, previous_ema_slow)  # next slow ema
        macd = fastMA - slowMA  # macd value
        signal_value = self.EMA(macd, signal, previous_macd)  # signal value
        return [macd, signal_value]

    def coins_instant_macd(
        self,
        symbol,
        fast,
        slow,
        signal,
        previous_ema_fast,
        previous_ema_slow,
        previous_macd,
    ):
        """
        * This function return instant macd using with the macd of the previous candlestick bars

        Note:
            * When the graphic move to a next candlestick bars you have to change the macd and run it again !
            * This function can't calculating next candlestick bars's macd. İt can just return instant macd !

        Examples
        - symbol = "BTCUSDT" string
        - fast = 12 int
        - slow = 26 int
        - signal = 9 int
        - previous_ema_fast
        - previous_ema_slow
        - previous_macd = 62017.40
        """
        close = price(self.client, symbol)
        return self.MACD(
            close,
            fast,
            slow,
            signal,
            previous_ema_fast,
            previous_ema_slow,
            previous_macd,
        )
