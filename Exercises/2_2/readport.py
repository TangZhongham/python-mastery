# readport.py

import csv


# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            record = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(record)
    return portfolio


if __name__ == '__main__':
    # portfolio = read_portfolio('../../Data/portfolio.csv')
    # from pprint import pprint
    # pprint(portfolio)

    from Exercises.one_six import readrides
    rows = readrides.read_rides_as_dic('../../Data/ctabus.csv')

    # 1. How many bus routes exist in Chicago?
    total_routes = len({s['route'] for s in rows})

    # 2. How many people rode the number 22 bus on February 2, 2011?
    # What about any route on any date of your choosing?
    # 5055
    population = sum([i['rides'] for i in rows if i['route']=='22'
                      and i['date']=='02/02/2011'])

    # 3. What is the total number of rides taken on each bus route?
    from collections import defaultdict,Counter
    totals = Counter()
    for s in rows:
        totals[s['route']] += s['rides']

    # 4
    rides_by_year = defaultdict(Counter)
    for row in rows:
        year = row['date'].split('/')[2]
        rides_by_year[year][row['route']] += row['rides']

    diffs = rides_by_year['2011'] - rides_by_year['2001']
    for route, diff in diffs.most_common(5):
        print(route, diff)






