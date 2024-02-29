def main():
    from sys import stdout
    N = int(input())
    vertical = '+' + '-'*N + '+'
    print(vertical)
    for _ in range(N):
        stdout.write(f'|{" "*N}|\n')
    print(vertical)


if __name__ == '__main__':
    main()
