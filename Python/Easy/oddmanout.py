def main():
    from collections import Counter
    for case_num in range(int(input())):
        input()
        guest_nums_counter = Counter(list(map(int, input().split())))
        print(f'Case #{case_num+1}: {guest_nums_counter.most_common()[len(guest_nums_counter)-1][0]}')


if __name__ == '__main__':
    main()