def main():
    input()
    words = input()
    print(''.join([word[0] for word in words.split() if word[0].isupper()]))


if __name__ == '__main__':
    main()
