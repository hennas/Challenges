def main():
    from sys import stdin
    s = 0
    for line in stdin.readlines()[1:]:
        g, b = map(int, line.split())
        if g+s >= b:
            s += g
        else:
            print('impossible')
            return
    print('possible')


if __name__ == '__main__':
    main()
