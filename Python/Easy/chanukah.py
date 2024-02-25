from sys import stdin, stdout
def func(val):
    idx = val.index(' ')
    days = int(val[idx:])
    stdout.write(f'{val[:idx]} {days*(days+1)//2 + days}\n')


if __name__ == '__main__':
    list(map(func, stdin.readlines()[1:]))
