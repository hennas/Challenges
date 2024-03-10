from sys import stdin


RING_GRID = []
X = 0
Y = 0
DELTA_FOR_4NHOOD = [(0,1), (0,-1), (1,0), (-1,0)]


def get_symbol_map(max_number):
    symbol_length = 2 if max_number < 10 else 3
    symbol_map = {0: '.' * symbol_length}
    for i in range(1, max_number+1):
        n = str(i)
        padding = symbol_length - len(n)
        symbol_map[i] = '.'*padding + n
    return symbol_map


def print_grid(total_rings):
    symbol_map = get_symbol_map(total_rings)
    for row in range(2, X+2):
        row_string = ''
        for col in range(2, Y+2):
            row_string += symbol_map[RING_GRID[row][col]]
        print(row_string)


def solve_next_tree_ring(index_set, next_ring):
    next_index_set = set()
    for row, col in index_set:
        for d in DELTA_FOR_4NHOOD:
            neighbor = RING_GRID[row + d[0]][col + d[1]]
            if neighbor == -1:
                RING_GRID[row + d[0]][col + d[1]] = next_ring
                next_index_set.add((row + d[0], col + d[1]))
    if next_index_set:
        return solve_next_tree_ring(next_index_set, next_ring+1)
    else:
        return next_ring - 1


def main():
    index_set = set()
    RING_GRID.extend([[0]*(Y+4), [0]*(Y+4)])
    index_set.update([(1, j) for j in range(1, Y+3)])
    for i, line in enumerate(stdin):
        line = '..' + line.rstrip() + '..'
        RING_GRID.append([])
        for j, c in enumerate(line):
            if c == '.':
                RING_GRID[i+2].append(0)
                if j != 0 and j != Y+3:
                    index_set.add((i+2, j))
            else:
                RING_GRID[i+2].append(-1)
    RING_GRID.extend([[0]*(Y+4), [0]*(Y+4)])
    index_set.update([(X+2, j) for j in range(1, Y+3)])
    total_rings = solve_next_tree_ring(index_set, 1)
    print_grid(total_rings)


if __name__ == '__main__':
    X, Y = map(int, next(stdin).split())
    main()
