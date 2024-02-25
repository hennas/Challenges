from sys import stdin

def main():
    info = stdin.readlines()
    print('777' if '7' in info[1] and '7' in info[2] and '7' in info[3] else '0')


if __name__ == '__main__':
    main()
