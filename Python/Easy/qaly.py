from sys import stdin

def main():
    print('%.3f' % sum([float(x)*float(y) for x,y in (val.split() for val in stdin.readlines()[1:])]))


if __name__ == '__main__':
    main()
