'''
to create the Stock class
'''
from .typedproperty import typedproperty

String = lambda name: typedproperty(name, str)
Integer = lambda name: typedproperty(name, int)
Float = lambda name: typedproperty(name, float)


class Stock:
    __slots__ = ('_name', '_shares', '_price')
    name = String('name')
    shares = Integer('shares')
    price = Float('price')
    def __init__(self, name=None, shares=0, price=0.0):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, num_shares=0):
        self.shares -= num_shares

    @property
    def shares(self):
        return self._shares
    
    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._shares = value

    def __repr__(self):
        return f'Stock({self.name}, {self.shares}, {self.price})'
