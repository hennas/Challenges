def main():
    num = int(input())
    while True:
        if num % sum(map(int, list(str(num)))) == 0:
            print(num)
            return
        num += 1


if __name__ == '__main__':
    main()
