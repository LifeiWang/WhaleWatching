import iexfinance
from iexfinance import stocks
from datetime import datetime
from datetime import timedelta
import pandas as pd
import ast


class IEXAccessor:

    IEX_ENDPOINT = "https://api.iextrading.com/1.0"

    @staticmethod
    def get_key_stat(symbol):
        stock = iexfinance.stocks.Stock(symbol, output_format='pandas')
        data = stock.get_key_stats()
        return data

    @staticmethod
    def get_finance(symbol):
        stock = iexfinance.stocks.Stock(symbol, output_format='pandas')
        data = stock.get_financials().T / 1000000
        return data

    @staticmethod
    def get_historical_data_1y(symbol):
        end = datetime.today()
        start = end - timedelta(days=365)
        df = stocks.get_historical_data(symbol, start, end, output_format='pandas')
        return df

    @staticmethod
    def get_historical_data_1m(symbol):
        end = datetime.today()
        start = end - timedelta(days=30)
        df = stocks.get_historical_data(symbol, start, end, output_format='pandas')
        return df

    @staticmethod
    def get_historical_data_2y(symbol):
        end = datetime.today()
        start = end - timedelta(days=730)
        df = stocks.get_historical_data(symbol, start, end, output_format='pandas')
        return df

    @staticmethod
    def get_sector_performance():
        df = stocks.get_sector_performance(output_format='pandas').T
        return df[['performance']]




