from sys import stdin
from math import sqrt


def print_result(corners, corner_info):
    n_of_corners = str(len(corners))
    res = ' '.join(map(lambda n: str(corner_info[n]['x'])
                       + ' ' + str(corner_info[n]['y']), corners))
    print(n_of_corners + ' ' + res)


def calc_neighbor_cosine(info, n_info, order=['right', 'left']):
    n_info[order[0] + 'x'] = info[order[0] + 'x'] - info[order[1] + 'x']
    n_info[order[0] + 'y'] = info[order[0] + 'y'] - info[order[1] + 'y']
    n_info[order[0] + 'l'] = sqrt(n_info[order[0] + 'x']**2 + n_info[order[0] + 'y']**2)
    n_cos = ((n_info['leftx']*n_info['rightx'] + n_info['lefty']*n_info['righty'])
             / (n_info['leftl']*n_info['rightl']))

    return n_cos


def cut_corners(corner_info, cosines, corners):
    sharpest_corner, max_cos = max(enumerate(cosines), key=lambda x: x[1])
    info = corner_info[sharpest_corner]

    left = info['leftn']
    l_info = corner_info[left]

    right = info['rightn']
    r_info = corner_info[right]

    l_cos = calc_neighbor_cosine(info, l_info)
    r_cos = calc_neighbor_cosine(info, r_info, ['left', 'right'])

    if l_cos > max_cos or r_cos > max_cos:
        return

    l_info['rightn'] = right
    r_info['leftn'] = left

    cosines[left] = l_cos
    cosines[right] = r_cos
    cosines[sharpest_corner] = -1

    corners.remove(sharpest_corner)

    cut_corners(corner_info, cosines, corners)


def main():
    for line in stdin:
        parts = list(map(int, line.split()))
        if len(parts) > 1:
            n_of_corners = parts[0]
            corners = list(n for n in range(n_of_corners))
            corner_info = {n: {} for n in corners}
            cosines = []
            for n in corners:
                x = parts[n*2+1]
                y = parts[n*2+2]
                left = (n+1) % n_of_corners # Left neighbor
                right = (n-1) % n_of_corners # Right neighbor
                left_x = parts[left*2+1] - x
                left_y = parts[left*2+2] - y
                left_length = sqrt(left_x**2 + left_y**2)
                right_x = parts[right*2+1] - x
                right_y = parts[right*2+2] - y
                right_length = sqrt(right_x**2 + right_y**2)
                cosines.append((left_x*right_x + left_y*right_y)
                                 / (left_length * right_length))

                corner_info[n]['x'] = x
                corner_info[n]['y'] = y
                corner_info[n]['leftn'] = left
                corner_info[n]['rightn'] = right
                corner_info[n]['leftx'] = left_x
                corner_info[n]['lefty'] = left_y
                corner_info[n]['leftl'] = left_length
                corner_info[n]['rightx'] = right_x
                corner_info[n]['righty'] = right_y
                corner_info[n]['rightl'] = right_length

            cut_corners(corner_info, cosines, corners)
            print_result(corners, corner_info)


if __name__ == '__main__':
    main()
