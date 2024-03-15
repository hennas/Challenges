def main():
    n = int(input())
    s = input().split()
    i = 13
    if n > i:
        print(s[i-1])
    else:
        print(s[i-(i//n)*n-1])


if __name__ == '__main__':
    main()
