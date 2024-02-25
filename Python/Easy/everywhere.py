def main():
    from sys import stdin
    inp = stdin.readlines()
    cities = []
    for val in inp[1:]:
        val = val.strip()
        if val.isnumeric() and len(cities) > 0:
            print(len(cities))
            cities = []
        if not val.isnumeric() and val not in cities:
            cities.append(val)
    print(len(cities))


if __name__ == '__main__':
    main()
