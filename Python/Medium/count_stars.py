DELTA_FOR_4NHOOD = [(0,1), (0,-1), (1,0), (-1,0)]


def find_star_neighbors(cell, star_cells, sky):
    row, col = cell
    for delta in DELTA_FOR_4NHOOD:
        neighbor = (row+delta[0], col+delta[1])
        if sky[neighbor[0]][neighbor[1]] == '-':
            star_cells.add(neighbor)


def count_stars(sky, X, Y):
    total_stars = 0
    for row in range(1, X+1):
        for col in range(1, Y+1):
            if sky[row][col] == '-':
                total_stars += 1
                star_cells = set()
                star_cells.add((row, col))
                while len(star_cells) > 0:
                    cell = star_cells.pop()
                    sky[cell[0]][cell[1]] = '#'
                    find_star_neighbors(cell, star_cells, sky)
    return total_stars


def main():
    case_n = 1
    while True:
        try:
            X, Y = map(int, input().split())
            sky = []
            sky.append(['#']*(Y+2))
            for _ in range(X):
                sky.append(list('#' + input() + '#'))
            sky.append(['#']*(Y+2))
            total_stars = count_stars(sky, X, Y)
            print(f'Case {case_n}:', total_stars)
            case_n += 1
        except EOFError:
            break


if __name__ == '__main__':
    main()
