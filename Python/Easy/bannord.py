def main():
    b, r = list(input()), ''
    for word in input().split():
        banned_found = False
        for banned in b:
            if banned in word and not banned_found:
                r += '*'*len(word)
                banned_found = True
                break
        if not banned_found:
            r += word
        r += ' '
    print(r.rstrip())


if __name__ == '__main__':
    main()
