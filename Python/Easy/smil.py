def main():
    s=input()
    for i in range(len(s)):
        x, y = s[i:i+2], s[i:i+3]
        if ':)' in x or ';)' in x:
            print(i)
        elif ':-)' in y or ';-)' in y:
            print(i)


if __name__ == '__main__':
    main()
