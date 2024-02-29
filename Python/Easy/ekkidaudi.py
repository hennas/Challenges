def main():
    from sys import stdin
    inp = [line.strip().split('|') for line in stdin.readlines()]
    print(f'{inp[0][0]}{inp[1][0]} {inp[0][1]}{inp[1][1]}')


if __name__ == '__main__':
    main()
