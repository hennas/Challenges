def main():
    from sys import stdin
    _, s = map(int, input().split())
    problems = stdin.readlines()
    for i in range(len(problems)):
        problems[i] = list(map(int, problems[i].split()))
    for problem in problems:
        if problem[0] <= s <= problem[1]:
            s += 1
    print(s)


if __name__ == '__main__':
    main()