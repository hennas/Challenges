def main():
    h, m = map(int, input().split())
    m -= 45
    if h == 0 and m < 0:
        h = 23
    elif m < 0:
        h -= 1
    if m < 0:
        m = 60 - abs(m)
    print(h, m)


if __name__ == '__main__':
    main()
