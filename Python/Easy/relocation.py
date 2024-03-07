def main():
    from sys import stdin
    _, Q = map(int, next(stdin).split())
    locations = list(map(int, next(stdin).split()))

    for _ in range(Q):
        req = list(map(int, next(stdin).split()))
        if req[0] == 1:
            locations[req[1]-1] = req[2]
        else:
            print(abs(locations[req[1]-1] - locations[req[2]-1]))


if __name__ == '__main__':
    main()
