def main():
    from sys import stdin
    inp = list(map(int, stdin.readlines()[1:]))
    print('\n'.join([str(val) for val in reversed(inp)]))


if __name__ == '__main__':
    main()
