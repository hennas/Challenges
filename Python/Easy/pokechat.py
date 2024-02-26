def main():
    s = input()
    n = input()
    idxs = list(map(int, [(n[i:i+3]) for i in range(0, len(n), 3)]))
    print(''.join(s[idx-1] for idx in idxs))


if __name__ == '__main__':
    main()
