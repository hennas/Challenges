from sys import stdin


X = 0
Y = 0
GRID = []
# Map that has 1 for cells that are "pools", 0 for those that are not, 
# and -1 for those that are still undetermined
POOL_CELLS = []
UNIQ_HEIGHTS = set()
DELTA_FOR_4NHOOD = [(0,1), (0,-1), (1,0), (-1,0)]


def find_neighbors_with_same_height(cell, height, found_neighbors, marked_cells):
    '''
    Checks the four adjacent neighbor cells of the given cell and adds them to 'found_neighbors'
    if they have the same height as the given cell and they are not included in the 'marked_cells'.
    '''
    row, column = cell
    for delta in DELTA_FOR_4NHOOD:
        neighbor = (row+delta[0], column+delta[1])
        neighbour_height = GRID[neighbor[0]][neighbor[1]]
        if neighbour_height == height and neighbor not in marked_cells:
            found_neighbors.add(neighbor)


def fill_pool_areas(comp_array, comp_value, fill_value):
    '''
    Fills those locations of POOL_CELLS with 'fill_value', where the corresponding
    locations in 'comp_array' have a value of 'comp_value'. 
    'comp_array' must have the same shape as POOL_CELLS.
    '''
    for row, values in enumerate(comp_array):
        for column, value in enumerate(values):
            if value == comp_value:
                POOL_CELLS[row][column] = fill_value


def solve():
    '''Finds the pool areas on a grid based on the height profile of the grid.'''

    min_height = min(UNIQ_HEIGHTS)
    # Any cell with minimum height is always a pool, because there is no cell of lower height
    fill_pool_areas(GRID, min_height, 1)

    max_height = max(UNIQ_HEIGHTS)
    # if max > min, no area with max height can be a pool
    if max_height > min_height:
        fill_pool_areas(GRID, max_height, 0)
    
    for row in range(1, Y+1):
        for column in range(1, X+1):
            # Going through the undetermined cells
            if POOL_CELLS[row][column] == -1:
                height = GRID[row][column]
                # The code below checks whether the cell has any neighbors with lower height, 
                # in which case the current cell cannot be a pool
                # Then, it iteratively marks every same-height neighbor cell with 0 (not a pool either)
                has_out_flow = False
                neighbors_with_same_height = set()

                for delta in DELTA_FOR_4NHOOD:
                    neighbor = (row+delta[0], column+delta[1])
                    neighbour_height = GRID[neighbor[0]][neighbor[1]]
                    if neighbour_height < height:
                        has_out_flow = True
                    elif neighbour_height == height:
                        neighbors_with_same_height.add(neighbor)

                if has_out_flow:
                    # Mark the current cell as not a pool
                    POOL_CELLS[row][column] = 0
                    # 'marked' set keeps track of all the marked cells in the same-height neighbourhood
                    marked = {(row, column)} 
                    while len(neighbors_with_same_height) > 0:
                        # Take out one same-height neighbor
                        neighbor = neighbors_with_same_height.pop()
                        # Mark it as not a pool
                        POOL_CELLS[neighbor[0]][neighbor[1]] = 0
                        # Add it into marked neighbourhood cells
                        marked.add(neighbor)
                        # Find the same-height neighbors of the current neighbor 
                        # and add them to neighbors_with_same_height set
                        find_neighbors_with_same_height(neighbor, height, neighbors_with_same_height, marked)

    # If there are any cells labeled -1 left, they must be pools
    fill_pool_areas(POOL_CELLS, -1, 1)


if __name__ == '__main__':
    X,Y = map(int, next(stdin).split())

    # This wall height is higher than the highest possible cell in the grid
    # according to the problem description
    wall_height = 1000

    # The grid is padded with the wall height to make it easier to check
    # the border areas of the grid
    GRID.append([wall_height]*(X+2))
    POOL_CELLS.append([0]*(X+2)) # Walls cannot be pools

    for i, line in enumerate(stdin):
        heights = list(map(int, line.split()))
        UNIQ_HEIGHTS.update(heights)
        GRID.append([wall_height] + heights + [wall_height])
        POOL_CELLS.append([0] + [-1]*X + [0])
    
    GRID.append([wall_height]*(X+2))
    POOL_CELLS.append([0]*(X+2))
    
    # Find areas that are pools
    solve()
    
    # Finally, print the result (the total number of cells marked as pools)
    n_of_pools = 0
    for values in POOL_CELLS:
        for value in values:
            n_of_pools += value
    print(n_of_pools)
