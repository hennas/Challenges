from sys import stdin


W = 0 # Width of the mosaic
H = 0 # Height
MOSAIC = [] # Instructions for creating the mosaic
GRID = [] # Placement of tiles
UNDETER = 0
BLACK = 1
WHITE = 2
UL = 4 # Upper left corner triangle
LL = 5 # Lower left corner triangle
LR = 6 # Lower right corner triangle
UR = 7 # Upper right corner triangle
TILES = [WHITE, UL, LL, LR, UR]

# Records what colors a triangular tile has towards the center of a 2x2 grid 
# depending on its position on the grid
COLORS = [[WHITE, WHITE], [BLACK, WHITE], [BLACK, BLACK], [WHITE, BLACK]]
# the index of the starting point for each type of tile is calculated with 
    # UL % 4, LL % 4, LR % 4, UR % 4
# the index of the colors towards the center, when the position of the tile 
# in the grid is either 0, 1, 2 or 3 is calculated with 
    # (starting_point + position) % 4
# (Position 0 is the upper left cell of a 2x2 grid, the other positions (1,2,3) 
# follow a clockwise direction from this)

# Only allowed sequences of white at the center of the 2x2 grid are 0, 2, 4 or 8, 
# corresponding to 0, 90, 180 and 360 degree "white" angles
ALLOWED_WHITES = [0,2,4,8]

DELTA_FOR_2X2 = [(0,0), (0,1), (1,1), (1,0)]
DELTA_FOR_4NHOOD = [(0,1), (0,-1), (1,0), (-1,0)]


def get_color_sequence(row, col):
    '''
    Returns a list of eight colors (either black, white or undetermined) 
    for the eight 45-degree angles at the center of a 2x2 grid.
    The colors start from the upper left cell of the 2x2 grid and continue 
    to the clockwise direction.
    The location of the upper left cell is given by parameters 'row' and 'col'.
    '''
    color_seq = []
    for position, delta in enumerate(DELTA_FOR_2X2):
        tile = int(GRID[row+delta[0]][col+delta[1]])
        if tile > WHITE: # Tile is a triangle
            colors_ind = ((tile % 4) + position) % 4
            colors_towards_center = COLORS[colors_ind]
            color_seq.extend(colors_towards_center)
        else: # Tile is black, white or undetermined
            color_seq.extend([tile]*2)
    return color_seq


def is_white_consistent(row, col):
    '''
    Checks whether the "white" angles at the center of 2x2 grid are either 
    0, 90, 180 or 360 degrees, which are the only possible values for a mosaic 
    in which any shape that remains white must be rectangular. 
    Returns True if the white angles are consistent with the above rule, otherwise False.
    Takes into account also the cells in the 2x2 grid that have no assigned tile yet.
    The location of the upper left cell of the 2x2 grid is given by parameters 'row' and 'col'.
    '''
    color_seq = get_color_sequence(row, col)
    # Duplicating the color_seq to account for the continuity from the 
    # lower left cell of the 2x2 grid to the upper left cell
    color_seq.extend(color_seq)
    
    n_of_whites = 0
    # The total number of whites only matters if we have 
    # encountered black and are counting from it
    counting_from_black = False
    for color in color_seq:
        if color == BLACK:
            # The only case where the white angles at the center of the 2x2 grid are inconsistent 
            # is when we have been counting whites from black to black and the number of whites 
            # between those is not in allowed_whites (that is, the "white" angle cannot be a part 
            # of a rectangle)
            if counting_from_black and n_of_whites not in ALLOWED_WHITES:
                return False
            n_of_whites = 0
            counting_from_black = True
        elif color == WHITE:
            n_of_whites += 1
        else: # Undetermined tile
            counting_from_black = False
    return True


def is_black_requirement_fulfilled(row, col):
    '''
    Checks the 4-neighbourhood of a black tile to see whether the number of 
    black triangles that share an edge with the black tile is consistent with 
    the requirement. Returns True if the requirement is fulfilled, otherwise False.
    '''
    if MOSAIC[row][col] == '*':
        return True
    requirement = int(MOSAIC[row][col])
    # Checking the tiles in the 4-neighbourhood of the black tile
    n_of_triangles = 0
    n_of_undeter = 0
    for delta in DELTA_FOR_4NHOOD:
        tile = GRID[row+delta[0]][col+delta[1]]
        if tile > WHITE:
            n_of_triangles += 1
        elif tile == UNDETER:
            n_of_undeter += 1 
    
    # Number of triangles around the black tile must fulfill the requirement, 
    # but it needs to be also checked that there is enough undetermined tiles 
    # for fulfilling the requirement
    requirement_ok = n_of_triangles <= requirement and n_of_triangles + n_of_undeter >= requirement
    return requirement_ok


def is_black_consistent(row, col):
    '''
    Checks whether the 4-neighbourhood of a location given by 
    (row,col) contains any black tiles.
    Every found black tile is checked to see whether its requirement 
    for the number of shared edges with black triangles is fulfilled. 
    Returns True if no violations are detected, otherwise False.
    '''
    for delta in DELTA_FOR_4NHOOD:
        nrow = row+delta[0]
        ncol = col+delta[1]
        if GRID[nrow][ncol] == BLACK:
            if not is_black_requirement_fulfilled(nrow, ncol):
                return False 
    return True


def fill_mosaic(row, col):
    '''
    Implements a backtracing search for the mosaic problem. 
    '''
    if row == H+1 and col == W+1:
        # We have reached the bottom right corner of the grid, which means that solution has been found
        # Print the number of triangles placed on the grid
        triangles = 0
        for row in GRID:
            for tile in row:
                if tile > WHITE:
                    triangles += 1
        print(triangles)
    else:
        if GRID[row][col] == BLACK:
            # Continue on the same row or move to the next row
            fill_mosaic(row+1,1) if col == W+1 else fill_mosaic(row, col+1)
        else:
            # Undetermined cell found, try possible tiles and check whether they are consistent with the rules
            for tile in TILES:
                GRID[row][col] = tile
                # Check if placement is consistent with the rules...
                # Every "white" angle at the center of a 2x2 grid should be either 360, 180, 90 or 0 degrees
                # Check consistency of "white" angles at every corner of the placed tile
                if (is_white_consistent(row-1,col-1) 
                    and is_white_consistent(row-1,col) 
                    and is_white_consistent(row,col-1) 
                    and is_white_consistent(row,col)):
                    # Check whether any cell in the 4-neighbourhood of the placed tile is black
                    # If a cell has a black tile, check consistency with the requirements of the black tile 
                    if is_black_consistent(row, col):
                        # Continue recursion if the placed tile is consistent with the rules
                        fill_mosaic(row, col+1)
                # If placement was not consistent, try the next tile or backtrack
                GRID[row][col] = UNDETER


def main():
    # Saving the instructions of the mosaic
    # Note that I'm padding the mosaic with unconstrained blacks to make it easier 
    # to check the consistency of placed tiles on the border areas
    MOSAIC.append('*' * (W+2))
    for line in stdin:
        MOSAIC.append('*' + line.rstrip() + '*')
    MOSAIC.append('*' * (W+2))

    # Creating a grid of the mosaic that only has black and undetermined tiles at the beginning
    for row in range(H+2):
        GRID.append([])
        for col in range(W+2):
            if MOSAIC[row][col] == '.':
                GRID[row].append(UNDETER)
            else:
                GRID[row].append(BLACK)
    
    # Backtracking search for finding the unique solution, starting from location (1,1) on the grid
    fill_mosaic(1,1)


if __name__ == '__main__':
    W,H = map(int, stdin.readline().split())
    main()
