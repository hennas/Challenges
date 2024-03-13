def main():
    from math import ceil
    n, m = int(input()), int(input())
    while n > 0:
        x = ceil(m/n)
        m -= x
        n -= 1
        print('*'*x)


if __name__ == '__main__':
    main()
