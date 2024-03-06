def main():
    print(sum([1 for i, c in enumerate(input()) if c != 'PER'[i%3]]))


if __name__ == '__main__':
    main()
