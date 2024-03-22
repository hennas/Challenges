def main():
    from sys import stdin, stdout
    for _ in range(int(next(stdin))):
        a, b, c = map(int, next(stdin).split())
        if a+b == c:
            stdout.write('Possible\n')
        elif a-b == c or b-a == c:
            stdout.write('Possible\n')
        elif a*b == c:
            stdout.write('Possible\n')
        elif a/b == c or b/a == c:
            stdout.write('Possible\n')
        else:
            stdout.write('Impossible\n')


if __name__ == '__main__':
    main()
