def read_portfolio(file_name):
    stocks = []
    import csv
    f = open(file_name)
    f_csv = csv.reader(f)
    headers = next(f_csv)
    rows = list(f_csv)
    return [Stock(name, int(shares), float(price)) for name, shares, price in rows]
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, sell_num):
        self.shares -= sell_num


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