
if __name__ == '__main__':

    sum_price = 0
    with open('../../Data/portfolio.dat', 'r') as f:
        for i in f.readlines():
            name, share, price = i.split()
            sum_price += float(share) * float(price)
    print("With total price of " + str(sum_price))
    print(f'With total price of {sum_price}')