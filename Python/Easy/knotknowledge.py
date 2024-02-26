def main():
    _ = input()
    learn = input().split()
    learned = input().split()
    print(list(set(learn)-set(learned))[0])


if __name__ == '__main__':
    main()
