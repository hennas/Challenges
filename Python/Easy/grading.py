def main():
    i=input().split()+[0]
    j=input()
    print('ABCDEF'[[int(j)>=int(x)for x in i].index(1)])


if __name__ == '__main__':
    main()
