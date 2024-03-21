def main():
    while(s:=input()) != '0 0':
        a, b = map(int, s.split())
        print(a//b, a%b, '/', b)


if __name__ == '__main__':
    main()
