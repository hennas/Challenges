def main():
    i = int(input())
    while i != -1:
        logs = [list(map(int, input().split())) for _ in range(i)]
        s = logs[0][0] * logs[0][1]
        for k in range(1, i):
            s += logs[k][0] * (logs[k][1] - logs[k-1][1])
        print(f'{s} miles')
        i = int(input())


if __name__ == '__main__':
    main()
