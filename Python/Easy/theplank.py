def main(n):
    if n < 0: return 0
    if n == 0: return 1
    return main(n-1) + main(n-2) + main(n-3)


if __name__ == '__main__':
    n = int(input())
    print(main(n))
