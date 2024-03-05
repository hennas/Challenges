def main():
    from sys import stdin
    cases = int(next(stdin))
    for case_num in range(cases):
        next(stdin)
        guest_nums = list(map(int, next(stdin).split()))
        unique_guest_nums = list(set(guest_nums))
        for guest_num in unique_guest_nums:
            if guest_nums.count(guest_num) == 1:
                print(f'Case #{case_num+1}: {guest_num}')
                break


if __name__ == '__main__':
    main()
