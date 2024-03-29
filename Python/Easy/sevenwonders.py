def main():
    from collections import Counter
    inp = Counter(input())
    s = sum([val**2 for val in inp.values()])
    vals = list(inp.values())
    if len(vals) == 3:
        while vals[0] > 0 and vals[1] > 0 and vals[2] > 0:
            s += 7
            vals[0] -= 1
            vals[1] -= 1
            vals[2] -= 1
    print(s)


if __name__ == '__main__':
    main()
