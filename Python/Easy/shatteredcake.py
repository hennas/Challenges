def main():
    from operator import mul
    W = int(input())
    print(sum([mul(val[0], val[1]) for val in [list(map(int, input().split())) for _ in range(int(input()))]] ) // W)


if __name__ == '__main__':
    main()
