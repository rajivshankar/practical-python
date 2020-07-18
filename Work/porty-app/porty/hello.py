def portfolio_cost(filename):
    total_price = 0.0
    with open(filename, 'rt') as f:
        heading = next(f)
        for line in f:
            name, quantity, price = line.split(',')
            item_price = float(quantity) * float(price)
            total_price += item_price
            # print(line.split(','))
            print(f' {name:>10s} {int(quantity): 5d} {float(price.strip()): 10.2f} {item_price: 10.2f}')
        print(f'Total Price: {total_price: 10.2f}')