def main():
    from sys import stdin
    n, _ = map(int, next(stdin).split())
    rungs = list(map(int, stdin.readlines()))
    result = {}
    for i in range(1, n+1):
        current = i
        for r in rungs:
            if current == r:
                current = r+1
            elif current-1 == r:
                current = r
        result[i] = current
    result = {k: v for k,v in sorted(result.items(), key=lambda i:i[1])}
    for i in result:
        print(i)


if __name__ == '__main__':
    main()
