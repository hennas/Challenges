def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        val1 = stdin.readline().strip()
        val2 = stdin.readline().strip()
        diff = ''.join([['*', '.'][val1[idx] == val2[idx]] for idx in range(len(val1))])
        stdout.write('\n'.join([val1, val2, diff])+'\n')


if __name__ == '__main__':
    main()
