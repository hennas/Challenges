def main():
    from sys import stdin
    inp = map(int, stdin.readlines())
    print(len(list(set([val % 42 for val in inp]))))


if __name__ == '__main__':
    main()
