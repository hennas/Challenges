def main():
    from sys import stdin, stdout
    for _ in range(int(next(stdin))):
        K, b, n = map(int, next(stdin).split())
        sum = 0
        while n > 0:
            sum += (n % b) * (n % b)
            n //= b
        stdout.write(f'{K} {sum}\n')


if __name__ == '__main__':
    main()
