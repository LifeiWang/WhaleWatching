
class StockDataFetcher:

    ALPHA_VANTAGE_KEY: str = "4TG666XGZMDE5LYL"
    IEX_URL = "https://api.iextrading.com/1.0"

    def generate_alpha_vantage_url(self, time_series: str, symbol: str) -> object:
        return "https://www.alphavantage.co/query?" + \
               "function=" + time_series + \
               "&symbol=" + symbol + \
               "&apikey=" + self.ALPHA_VANTAGE_KEY





