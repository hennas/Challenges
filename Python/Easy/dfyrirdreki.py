from math import sqrt


def calc_root(a,b,c,op):
    try:
        if op == '+':
            return (-b + sqrt(b**2-4*a*c)) / (2*a)
        else:
            return (-b - sqrt(b**2-4*a*c)) / (2*a)
    except ValueError:
        return None


def main():
    a, b, c = map(int, [input(), input(), input()])
    r1 = calc_root(a,b,c,'+')
    r2 = calc_root(a,b,c,'-')
    if r1 is not None and r1 == r2:
        print(1)
    else:
        print(2-[r1,r2].count(None))


if __name__ == '__main__':
    main()
