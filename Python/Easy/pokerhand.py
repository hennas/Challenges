def main():
    from collections import Counter
    print(Counter(list(map(lambda x: x[0], input().split()))).most_common()[0][1])


if __name__ == '__main__':
    main()
