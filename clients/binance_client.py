from binance.client import Client
from binance import exceptions


class BinanceClient:

    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret)

    def get_all_prices(self):
        try:
            return self.client.get_all_tickers()
        except (exceptions.BinanceRequestException, exceptions.BinanceAPIException) as exc:
            print(exc)
            return

    def get_price(self, ticket):
        prices = self.get_all_prices()
        if not prices:
            return
        for price in prices:
            if price.get('symbol') == ticket:
                return price.get('price')

    def get_clines(self, ticket):
        return self.client.get_historical_klines(ticket, Client.KLINE_INTERVAL_1MINUTE, "1 day ago UTC")
