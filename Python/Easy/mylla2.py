def main():
    s = [input(), input(), input()]
    if 'OOO' in s:
        print('Jebb')
        return
    for i in range(3):
        if s[0][i] == 'O' and s[1][i] == 'O' and s[2][i] == 'O':
            print('Jebb')
            return
    if s[0][0] == 'O' and s[1][1] == 'O' and s[2][2] == 'O' or \
       s[0][2] == 'O' and s[1][1] == 'O' and s[2][0] == 'O':
        print('Jebb')
        return
    print('Neibb')


if __name__ == '__main__':
    main()
