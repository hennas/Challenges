def main():
    result = 0
    n = int(input())
    prev_val = list(map(float, input().split()))
    for _ in range(n-1):
        current_val = list(map(float, input().split()))
        result += (current_val[1]+prev_val[1])/2*(current_val[0]-prev_val[0]) / 1000
        prev_val = current_val
    print(result)


if __name__ == '__main__':
    main()
