def main():
    n, m = map(int, input().split())
    a = [' '] * (m-n) + list(input())
    b = input()
    for i in range(m-1, n-1, -1):
        a[i-n] = chr(ord('a') + (26 + ord(b[i]) - ord(a[i])) % 26)
    print(''.join(a))


if __name__ == '__main__':
    main()
