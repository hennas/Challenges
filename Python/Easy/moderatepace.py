from sys import stdin

def get_int_list_from_input():
    return list(map(int, next(stdin).split()))

def main():
    num_days = int(next(stdin))
    l1 = get_int_list_from_input()
    l2 = get_int_list_from_input()
    l3 = get_int_list_from_input()
    print(' '.join([str(sorted([l1[i], l2[i], l3[i]])[1]) for i in range(num_days)]))


if __name__ == '__main__':
    main()
