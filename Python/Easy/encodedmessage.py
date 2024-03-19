def main():
    from math import sqrt
    for _ in range(int(input())):
        s=input()
        l=int(sqrt(len(s)))
        s = [s[i:i+l] for i in range(0,len(s), l)]
        s2 = ''
        for i in range(len(s)-1, -1, -1):
            for j in range(0, len(s)):
                s2 += s[j][i]
        print(s2)


if __name__ == '__main__':
    main()
