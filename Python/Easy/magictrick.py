def main():
    inp = input()
    for c in [*'abcdefghijklmnopqrstuvwxyz']:
        if inp.count(c) > 1:
            print(0)
            return
    print(1)

if __name__ == '__main__':
    main()
