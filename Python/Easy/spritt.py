def main():
    from sys import stdin
    needed, s = int(input().split()[1]), 0
    for line in stdin:
        s += int(line)
        if s > needed:
            print("Neibb")
            return
    print('Jebb')

if __name__ == '__main__':
    main()