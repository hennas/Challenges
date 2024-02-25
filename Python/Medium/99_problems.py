import sys

price = next(sys.stdin).strip()
price_99 = price[:-2] + '99'
if len(price_99) > 2 and int(price_99) - int(price) > 50:
    start = int(price[:-2]) - 1
    sys.stdout.write(f'{start * 100 + 99}')
else:
    sys.stdout.write(price_99)
