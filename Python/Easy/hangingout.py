def main():
    L, i = map(int, input().split())
    num_people, r = 0, 0
    for _ in range(i):
        s = input().split()
        s[1] = int(s[1])
        if s[0] == 'enter':
            if num_people + s[1] > L:
                r+=1
            else:
                num_people += s[1]
        else:
            num_people -= s[1]
    print(r)


if __name__ == '__main__':
    main()
