def main():
    s = input().split(';')
    r = 0
    for t in s:
        if '-' in t:
            t = list(map(int, t.split('-')))
            r += len(range(t[0], t[1]+1))
        else:
            r += 1
    print(r)


if __name__ == '__main__':
    main()
