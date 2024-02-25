def main():
    from sys import stdin
    stdin.readline()
    for line in stdin:
        num, days = map(int, line.split())
        candles = sum([c+1 for c in range(1,days+1)])
        print(f'{num} {candles}')

if __name__ == '__main__':
    main()
