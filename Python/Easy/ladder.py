def main():
    from math import sin, radians, ceil
    h, w = map(int, input().split())
    print(ceil(h / sin(radians(w))))


if __name__ == '__main__':
    main()
