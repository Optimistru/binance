import time

from clients import binance_client
from clients import talib_client

import settings


class Controller:
    def __init__(self):
        self.binance = binance_client.BinanceClient(settings.API_KEY, settings.API_SECRET)
        self.math = talib_client.MathClient()

    def solver(self):
        prices = []
        while True:
            price = self.binance.get_price("BTCUSDT")
            prices.append(float(price))
            print(self.math.MA(array=prices, timeperiod=99)[-1])
            time.sleep(0.3)



if __name__ == "__main__":
    controller = Controller()
    while True:
        controller.solver()
