from sys import stdin


def main():
    orig = next(stdin).rstrip()
    o_len = len(orig)

    infected = next(stdin).rstrip()
    i_len = len(infected)

    start = -1
    for i, n in enumerate(infected):
        if i == o_len or n != orig[i]:
            start = i
            break

    end = -1
    for i in range(-1, -(i_len+1), -1):
        if i == -(o_len+1) or infected[i] != orig[i]:
            end = i_len + i
            break

    if start == -1 or start > end:
        if o_len >= i_len:
            print(0)
        else:
            print(i_len - o_len)
    else:
        print(end - start + 1)


if __name__ == '__main__':
    main()
