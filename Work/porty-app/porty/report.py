# report.py
#
# Exercise 2.4

import sys
import csv
from . import fileparse
from . import stock
from . import tableformat
from .portfolio import Portfolio


def read_portfolio(filename = './Data/portfolio.csv', **opts):
    '''
    Computes the total cost (shares * price) of a portfolio file
    '''
    with open(filename) as file:
#         portdicts = fileparse.parse_csv(filename, **opts)
        portfolio = Portfolio.from_csv(file)

#     portfolio = [stock.Stock(**d) for d in portdicts]
    return portfolio


def read_prices(filename='./Data/prices.csv',
                types=[str, float]) -> dict:
    '''Reads prices and returns a dict of stock and prices'''
    with open(filename) as file:
        prices_tuples = fileparse.parse_csv(
            file, has_headers=False, types=types)
    prices = {k: v for k, v in prices_tuples}
    return prices


def compute_portfolio_value():
    '''Takes the portfolio and computes the current value and the gain/loss'''
    portfolio_cost = 0.0
    portfolio_value = 0.0
    portfolio = read_portfolio('./Data/portfolio.csv',
                               select=['name', 'shares', 'price'],
                               types=[str, int, float])
    prices = read_prices('./Data/prices.csv', types=[str, float])

    for stock in portfolio:
        portfolio_cost += int(stock['shares']) * float(stock['price'])
        portfolio_value += int(stock['shares']) * \
            float(prices.get(stock['name'], stock['price']))

    print(f'Portfolio Cost: {portfolio_cost: 0.2f}')
    print(f'Portfolio Value: {portfolio_value: 0.2f}')
    print(f'Portfolio gain/loss: {portfolio_value - portfolio_cost: 0.2f}')


def make_report_data(portfolio, prices):
    '''takes a list of dict (portfolio) and dicts (prices) and returns tuple'''
    report_rows = []
    for stock in portfolio:
        report_rows.append(
            (
                stock.name,
                stock.shares,
                prices.get(stock.name, stock.price),
                prices.get(stock.name, stock.price) - stock.price
            )
        )
    return report_rows

def temp_func(*args, **kwargs):
    '''This is a temporatry function to test gvim'''
    pass


def portfolio_report(portfolio_filename='./Data/portfolio.csv',
                     prices_filename='./Data/prices.csv',
                     fmt='txt'):
    '''
    Takes portfolio file and prices file and creates portfolio report
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename,
                               select=['name', 'shares', 'price'],
                               types=[str, int, float])
    prices = read_prices(prices_filename, types=[str, float])

    # Create report data
    report = make_report_data(portfolio, prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, share, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [name, str(shares), f'{price:0.2f}', f'{change:0.2f}']
        formatter.row(rowdata)


def main(args):
    try:
        portfolio_report(args[1], args[2], args[3])
    except Exception as e:
        print ("Unexpected error: ", e)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)

# This file sets up basic configuration of the logging module.
# Change settings here to adjust logging output as needed.
import logging
logging.basicConfig(
    filename = 'app.log',            # Name of the log file (omit to use stderr)
    filemode = 'w',                  # File mode (use 'a' to append)
    level    = logging.WARNING,      # Logging level (DEBUG, INFO, WARNING, ERROR, or CRITICAL)
)