def main():
    n = int(input())
    if n%2 == 1:
        print('still running')
    else:
        print(sum([-int(input()) + int(input()) for _ in range(n//2)]))


if __name__ == '__main__':
    main()
