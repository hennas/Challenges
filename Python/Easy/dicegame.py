def main():
    sum_g = sum(map(int, input().split()))
    sum_e = sum(map(int, input().split()))

    if sum_g > sum_e:
        print('Gunnar')
    elif sum_e > sum_g:
        print('Emma')
    else:
        print('Tie')


if __name__ == '__main__':
    main()
