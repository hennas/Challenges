def main():
    inp = input()
    print(sum([1 for val in inp if val in ['a', 'e', 'i', 'o', 'u']]), sum([1 for val in inp if val in ['a', 'e', 'i', 'o', 'u', 'y']]))


if __name__ == '__main__':
    main()
