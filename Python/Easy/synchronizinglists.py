def main():
    from sys import stdin, stdout
    while (l := int(next(stdin))) != 0:
        l1, l2 = [], []
        for _ in range(l):
            l1.append(int(next(stdin)))
        for _ in range(l):
            l2.append(int(next(stdin)))
        l1dict = {k:v for k, v in zip(sorted(l1), sorted(l2))}
        for k in l1:
            stdout.write(f'{l1dict[k]}\n')


if __name__ == '__main__':
    main()
