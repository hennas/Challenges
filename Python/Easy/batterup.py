def main():
    input()
    inp = list(filter(lambda x: x>= 0, map(int, input().split())))
    print(sum(inp)/len(inp))


if __name__ == '__main__':
    main()
