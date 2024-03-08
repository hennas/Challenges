def main():
    s, t, n = map(int, input().split())
    d = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    s += d[0]
    for i in range(n):
        while s % c[i] != 0:
            s += 1
        s += b[i] + d[i+1]

    if s <= t:
        print('yes')
    else:
        print('no')


if __name__ == '__main__':
    main()
