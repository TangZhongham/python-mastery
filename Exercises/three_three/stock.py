from decimal import Decimal
import csv
def read_portfolio(file_name):
    stocks = []
    import csv
    f = open(file_name)
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rows = list(f_csv)
    return [Stock.from_row(row) for row in rows]


def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

class Stock:
    types = (str, int, float)
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        return self.shares * self.price

    def sell(self, sell_num):
        self.shares -= sell_num


class DStock(Stock):
    types = (str, int, Decimal)


def print_portfolio(portfolio: [Stock]):
    '''
    Make a nicely formatted table showing stock data
    '''
    print('%10s %10s %10s' % ('name', 'shares', 'price'))
    print(('-'*10 + ' ')*3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name, s.shares, s.price))



if __name__ == '__main__':
    s = Stock('GOOG', 100, 490.10)
    s.sell(25)
    print(s.shares)
    portfolio = read_portfolio('../../Data/portfolio.csv')
    print_portfolio(portfolio)

    # row = ['AA', '100', '32.20']
    # s = DStock.from_row(row)
    # print(type(s.price))