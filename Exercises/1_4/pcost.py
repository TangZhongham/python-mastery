
def portfolio_cost(file_dir: str):
    sum_price = 0
    with open(file_dir, 'r') as f:
        for i in f.readlines():
            name, share, price = i.split()
            try:
                sum_price += float(share) * float(price)
            except ValueError as e:
                print(f"Couldn't parse {repr(i)}")
                print(f"Reason: {e}")
    print("With total price of " + str(sum_price))
    return f'With total price of {sum_price}'


if __name__ == '__main__':
    file = '../../Data/portfolio3.dat'
    print(portfolio_cost(file))