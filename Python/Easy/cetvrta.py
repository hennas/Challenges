def main():
    from sys import stdin
    x_points, y_points = [], []
    for entry in stdin:
        x, y = map(int, entry.split())
        x_points.append(x)
        y_points.append(y)
    print(f'{[x for x in x_points if x_points.count(x) == 1][0]} {[y for y in y_points if y_points.count(y) == 1][0]}')


if __name__ == '__main__':
    main()
