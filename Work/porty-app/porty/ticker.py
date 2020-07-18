# ticker.py

from follow import follow
import csv
from . import report
from . import tableformat

def filter_symbols(rows, names):
    for row in rows:
        if row['name'] in names:
            yield row

def convert_types(rows, types):
    for row in rows:
        yield[func(val) for func, val in zip(types, row)]
        
def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))


def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]


def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfolio_file='./Data/portfolio.csv',
           logfile='./Data/stocklog.csv',
           fmt='txt'):
    portfolio = report.read_portfolio(portfolio_file)
    rows = parse_stock_data(follow(logfile))
    rows = (row for row in rows if row['name'] in portfolio)
    
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        rowdata = [row["name"], f'{row["price"]:0.2f}', f'{row["change"]:0.2f}']
        formatter.row(rowdata)


if __name__ == '__main__':
    portfolio = report.read_portfolio('./Data/portfolio.csv')
    lines = follow('./Data/stocklog.csv')
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
        
