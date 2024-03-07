def main():
    from sys import stdin
    zero_car, one_car, two_cars, three_cars, four_cars = 0, 0, 0, 0, 0
    inp = list(map(str. strip, stdin.readlines()[1:]))
    for i in range(1, len(inp)):
        for j in range(1, len(inp[i])):
            combined_spaces = inp[i-1][j-1] + inp[i-1][j] + inp[i][j-1] + inp[i][j]
            if '#' in combined_spaces:
                continue
            num_cars = combined_spaces.count('X')
            if num_cars == 0:
                zero_car += 1
            elif num_cars == 1:
                one_car += 1
            elif num_cars == 2:
                two_cars += 1
            elif num_cars == 3:
                three_cars += 1
            else:
                four_cars += 1

    print(zero_car)
    print(one_car)
    print(two_cars)
    print(three_cars)
    print(four_cars)


if __name__ == '__main__':
    main()
