def main():
    x, y = map(int, input().split())
    print('possible' if (x*4+y*3)%2 == 0 else 'impossible')


if __name__ == '__main__':
    main()
