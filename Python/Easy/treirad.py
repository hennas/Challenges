def main():
    n = int(input())
    i, c, t = 0, 1, 0
    while i < n:
        i = c*(c+1)*(c+2)
        if i < n:
            t += 1
        c += 1
    print(t)


if __name__ == '__main__':
    main()
