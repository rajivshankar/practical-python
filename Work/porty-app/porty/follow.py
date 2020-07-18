# follow.py
import os
import time
from . import report
from . import portfolio

def follow(filename='Data/stocklog.csv',
           portfolio_filename='Data/portfolio.csv'):
    f = open(filename)
    f.seek(0, os.SEEK_END) # Move file pointer 0 bytes from end of file
    
    portfolio=report.read_portfolio(filename=portfolio_filename,
                                    select=['name', 'shares', 'price'],
                                    types=[str, int, float])

    while True:
        line = f.readline()
        if line == '':
            time.sleep(0.1)
            continue
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if name in portfolio:
            # yield(f'{name:>10s} {price:10.2f} {change:>10.2f}\n')
            yield line