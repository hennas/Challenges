def main():
    inp = input().replace('-', '')
    multipliers = [4,3,2,7,6,5,4,3,2,1]
    print(1 if sum([int(val)*multipliers[i] for i, val in enumerate(inp)]) % 11 == 0 else '0')


if __name__ == '__main__':
    main()
