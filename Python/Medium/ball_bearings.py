from math import floor, asin, pi


for _ in range(int(input())):
    D, d, s = map(float, input().split())
    print(floor(pi / (asin((d+s) / (D-d)))))
