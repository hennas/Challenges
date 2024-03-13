def main():
    s = input()
    r = ''
    for i in range(0, len(s)-1):
        if s[i] != s[i+1]:
            r += s[i]
    if r[-1] != s[-1]:
        r += s[-1]
    print(r)


if __name__ == '__main__':
    main()
