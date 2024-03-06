def main():
    for _ in range(int(input())):
        vals = list(map(int, input().split()[:-1]))
        diff = 0
        for i in range(len(vals)-1):
            if vals[i+1] > vals[i]*2:
                diff += vals[i+1] - vals[i]*2
        print(diff)


if __name__ == '__main__':
    main()
