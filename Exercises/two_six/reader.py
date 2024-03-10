import csv


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


class Reader:
    def read_csv_as_dicts(self, filename, type_list):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = {name: func(val) for name, func, val in zip(headers, type_list, row)}
                records.append(record)
        return records




if __name__ == '__main__':
    portfolio = Reader().read_csv_as_dicts('../../Data/portfolio.csv', [str, int, float])
    for i in portfolio:
        print(i)