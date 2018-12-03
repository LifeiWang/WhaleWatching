
class TechnicalIndicator:

    @staticmethod
    def moving_average_50(data_frame):
        return data_frame.loc['day50MovingAvg'][0]

    @staticmethod
    def moving_average_200(data_frame):
        return data_frame.loc['day200MovingAvg'][0]

    @staticmethod
    def price_to_book(data_frame):
        return data_frame.loc['priceToBook'][0]

    @staticmethod
    def price_to_sale(data_frame):
        return data_frame.loc['priceToSales'][0]

