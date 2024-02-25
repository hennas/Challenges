def main():
    N, M = map(int, input().split())
    r = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            r.append(i+j)
    r2 = {}

    for val in set(r):
        r2[val] = round(r.count(val) / len(r), 3)
    r2 = sorted(r2.items(), key=lambda x:x[1], reverse=True)

    prob = None
    for val in r2:
        if prob is None:
            prob = val[1]
            print(val[0])
        elif prob is not None and prob == val[1]:
            print(val[0])


if __name__ == '__main__':
    main()
