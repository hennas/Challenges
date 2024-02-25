from sys import stdin
from math import floor


def calculate_waste_amount(requirement, can_sizes, min_index, max_index):
    if max_index - min_index == 1:
        if can_sizes[min_index] < requirement:
            return can_sizes[max_index] - requirement
        else:
            return can_sizes[min_index] - requirement
    middle = min_index + floor((max_index - min_index) / 2)
    size = can_sizes[middle]
    if size == requirement:
        return 0
    elif size < requirement:
        min_index = middle
        return calculate_waste_amount(requirement, can_sizes, min_index, max_index)
    else:
        max_index = middle
        return calculate_waste_amount(requirement, can_sizes, min_index, max_index)


def parse_quantities_from_input(n_of_lines):
    quantities = []
    while n_of_lines > 0:
        quantities.append(int(stdin.readline()))
        n_of_lines -= 1
    return quantities


def get_input_info():
    n_of_sizes, n_of_colors = map(int, stdin.readline().split())
    can_sizes = parse_quantities_from_input(n_of_sizes)
    color_needs = parse_quantities_from_input(n_of_colors)
    return can_sizes, color_needs


if __name__ == '__main__':
    can_sizes, color_needs = get_input_info()
    can_sizes.sort()
    wasted_paint = 0
    min_index = 0
    max_index = len(can_sizes)
    for amount in color_needs:
        wasted_paint += calculate_waste_amount(amount, can_sizes, min_index, max_index)
    print(wasted_paint)
