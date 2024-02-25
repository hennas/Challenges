def main():
    from sys import stdin
    amt = int(stdin.readline())
    for _ in range(amt):
        val1 = stdin.readline().strip()
        val2 = stdin.readline().strip()
        diff = ''
        for i, chr in enumerate(val1):
            if val2[i] != chr:
                diff += '*'
            else:
                diff += '.'
        print(val1)
        print(val2)
        print(diff)

if __name__ == '__main__':
    main()
