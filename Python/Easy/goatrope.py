def main():
    x, y, x1, y1, x2, y2 = map(float, input().split())
    if x1 <= x <= x2:
        print(y1-y if y1 > y else y-y2)
    elif y1 <= y <= y2:
        print(x1-x if x1 > x else x-x2)
    else:
        x3 = [x2,x1][abs(x-x1) < abs(x-x2)]
        y3 = [y2,y1][abs(y-y1) < abs(y-y2)]
        print(((x - x3)**2 + (y - y3)**2)**0.5)


if __name__ == '__main__':
    main()
