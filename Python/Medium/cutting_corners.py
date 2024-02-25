import sys


if __name__ == "__main__":
    for line in sys.stdin:
        parts = list(map(int, line.split()))
        if len(parts) > 1:
            corners = parts[0]
            corner_n = list(n for n in range(corners))
            corner_info = {n: {} for n in corner_n}
            dot_prods = []
            for n in corner_n:
                x = parts[n*2+1]
                y = parts[n*2+2]
                left = (n+1) % corners
                right = (n-1) % corners
                left_x = parts[left*2+1] - x
                left_y = parts[left*2+2] - y
                right_x = parts[right*2+1] - x
                right_y = parts[right*2+2] - y
                dot_prods.append(left_x*right_x + left_y*right_y)
                corner_info[n]['x'] = x
                corner_info[n]['y'] = y
                corner_info[n]['leftx'] = left_x
                corner_info[n]['lefty'] = left_y
                corner_info[n]['rightx'] = right_x
                corner_info[n]['righty'] = right_y
            print(corner_info)
            print(dot_prods)

