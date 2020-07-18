# pcost.py
#
# Exercise 1.27
import sys
import csv
from . import report
from .portfolio import Portfolio


def portfolio_cost(filename='./Data/portfolio.csv'):
    total_price = 0.0

    portfolio = report.read_portfolio(filename,
                                 select=['name', 'shares', 'price'],
                                 types=[str, int, float])

    return portfolio.total_cost


def main(filenames):
    portfolio_cost(filenames[1])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv)
