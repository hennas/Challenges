def main():
    from sys import stdin
    _, days_to_b_day, current_day = map(int, input().split())
    print( sum([1 for q in stdin.readlines() if abs(days_to_b_day - int(q) + current_day) >= 14]) )


if __name__ == '__main__':
    main()
