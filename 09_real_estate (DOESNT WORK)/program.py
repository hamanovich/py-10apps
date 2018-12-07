import os
import csv

from data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('REAL ESTATE APP')
    print('===============')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'realestate.csv')


def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(row)

        return purchases

def get_price(p):
    return p['price']

def query_data(data):
    data.sort(key=get_price)
    print(data)
    high_purchase = data[-1]
    low_purchase = data[0]

    print(high_purchase['price'])
    print('{:,}'.format(float(low_purchase['price'])))


if __name__ == "__main__":
    main()
