def main():
    inp = input()
    name = ['P', 'E', 'R']
    ctr = 0
    r = 0
    for i in range(len(inp)):
        if inp[i] != name[ctr]:
            r += 1
        ctr += 1
        if ctr != 0 and ctr % 3 == 0:
            ctr = 0
    print(r)


if __name__ == '__main__':
    main()
