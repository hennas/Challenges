def main():
    from sys import stdin
    W = int(input())
    print(sum([val[0] * val[1] for val in [list(map(int, next(stdin).split())) for _ in range(int(next(stdin)))]] ) // W)


if __name__ == '__main__':
    main()
