from sys import stdin

def main():
    info = stdin.readlines()
    if '7' in info[1] and '7' in info[2] and '7' in info[3]:
        print('777')
    else:
        print(0)


if __name__ == '__main__':
    main()
