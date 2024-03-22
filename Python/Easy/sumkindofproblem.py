def main():
    from sys import stdin, stdout
    nums = range(1,10_000+1)
    odd_nums = [1+2*i for i in range(10_000)]
    even_nums = [2+2*i for i in range(10_000)]
    for _ in range(int(next(stdin))):
        K, N = map(int, next(stdin).split())
        s1 = sum(nums[:N])
        s2 = sum(odd_nums[:N])
        s3 = sum(even_nums[:N])
        stdout.write(f'{K} {s1} {s2} {s3}\n')


if __name__ == '__main__':
    main()
