def main():
    from sys import stdin
    r = ''
    for line in stdin.readlines()[1:]:
        r += ''.join([chr for chr in line.strip() if chr != '.'])
    print(r)


if __name__ == '__main__':
    main()
