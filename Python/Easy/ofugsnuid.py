def main():
    from sys import stdin
    inp = list(map(int, stdin.readlines()[1:]))
    for val in reversed(inp):
        print(val)


if __name__ == '__main__':
    main()
