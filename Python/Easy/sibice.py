def main():
    from sys import stdin
    from math import sqrt
    _, W, H = map(float, input().split())
    for l in stdin:
        print('DA' if int(l) <= sqrt(W**2 + H**2) else 'NE')


if __name__ == '__main__':
    main()
