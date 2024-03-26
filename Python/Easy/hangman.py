def main():
    s = list(input())
    q = input()
    quesses_left, ctr = 10, 0

    for c in q:
        if ctr == len(set(s)):
            break
        if c in s:
            ctr += 1
        else:
            quesses_left -= 1
    print('WIN' if quesses_left > 0 else 'LOSE')


if __name__ == '__main__':
    main()
