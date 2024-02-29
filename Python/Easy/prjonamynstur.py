def main():
    from sys import stdin
    symbol_len = {
        '.': 20, 'O': 10, '\\': 25, '/': 25,
        'A': 35, '^': 5, 'v': 22
    }
    s = 0
    for line in stdin.readlines()[1:]:
        s += sum([symbol_len[symbol] for symbol in line.strip()])
    print(s)


if __name__ == '__main__':
    main()
