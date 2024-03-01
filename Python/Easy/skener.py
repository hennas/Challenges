def main():
    from sys import stdin
    _, _, Z_R, Z_C = map(int, input().split())
    for line in stdin:
        print('\n'.join([''.join([chr*Z_C for chr in line.strip()])]*Z_R))


if __name__ == '__main__':
    main()
