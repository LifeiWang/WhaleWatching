import iexfinance.stocks
from Data.IEXAccessor import IEXAccessor


def write_to_file(file_name, data_frame):
    data_frame.to_csv(file_name, sep='\t')


if __name__ == "__main__":

    symbol = 'NFLX'
    # df = IEXAccessor.get_key_stat('AAPL')
    # df = IEXAccessor.get_historical_data('FB')
    # df = IEXAccessor.get_sector_performance()
    df = IEXAccessor.get_finance(symbol)
    print(df)
    write_to_file('finance/' + symbol + '_finance.csv', df)


