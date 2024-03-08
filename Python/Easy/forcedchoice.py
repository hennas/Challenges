def main():
    from sys import stdin
    N, P, S = map(int, input().split())
    for line in stdin:
        print('KEEP' if P in map(int, line.split()[1:]) else 'REMOVE')


if __name__ == '__main__':
    main()
