def main():
    inp = input()
    if len(inp) == 10:
        print(-1)
        return
    for i, num in enumerate(inp):
        if num != f'{i+1}':
            print(-1)
            return
    print(inp[-1])


if __name__ == '__main__':
    main()
