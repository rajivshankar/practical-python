# tableformat.py

class TableFormatter:
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        print(','.join(headers))

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        '''
        Emit the table headings
        '''
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        '''
        Emit a single row of table data
        '''
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

class FormatError(Exception):
    pass


def create_formatter(fmt='txt'):
    if fmt == 'txt':
        formatter = TextTableFormatter()
    elif fmt == 'csv':
        formatter = CSVTableFormatter()
    elif fmt == 'html':
        formatter = HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown format {fmt}')

    return formatter


def print_table(portfolio, select, formatter):

    formatter.headings(select)
    for stock in portfolio:
        stock_row = []
        for colname in select:
            col_value = getattr(stock, colname)

            if type(col_value) == 'int':
                col_value = str(col_value)
            elif type(col_value) == 'float':
                col_value=f'{col_value:0.2f}'
            stock_row.append(col_value)

        formatter.row(stock_row)