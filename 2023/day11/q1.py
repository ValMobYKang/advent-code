from itertools import combinations
from collections import deque
# Read the input grid from a text file
with open('puzzle', 'r') as file:
    puzzle = file.read()

grid = [list(row) for row in puzzle.splitlines()]

def expand_universe(grid):
    # Convert the input grid into a list of lists for easier manipulation
    
    height = len(grid)
    width = len(grid[0])

    # Identify empty rows and columns
    empty_rows = {i for i in range(height) if all(cell == '.' for cell in grid[i])}
    empty_cols = {j for j in range(width) if all(grid[i][j] == '.' for i in range(height))}
    
    # Expand empty rows
    new_grid = []
    for i in range(height):
        if i in empty_rows:
            new_grid.append(grid[i])
        new_grid.append(grid[i])
    
    # Transpose the grid to expand columns easily
    transposed_grid = list(map(list, zip(*new_grid)))

    # Expand empty columns
    expanded_grid = []
    for j in range(len(transposed_grid)):
        if j in empty_cols:
            expanded_grid.append(transposed_grid[j])
        expanded_grid.append(transposed_grid[j])

    # Transpose back to the original orientation
    final_grid = list(map(list, zip(*expanded_grid)))

    # DEBUG
    # print('\n'.join(''.join(row) for row in final_grid))

    # Convert the list of lists back into a string representation
    return final_grid 

def find_galaxies(grid):
    # Initialize an empty list to store the positions of the galaxies
    galaxies_positions = []

    # Iterate over each cell in the grid to find galaxies
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '#':
                # Save the position as a tuple (row, column)
                galaxies_positions.append((i, j))
    
    return galaxies_positions

# def bfs_shortest_path(start,end):
#     directions = [(-1,0),(1,0),(0,-1),(0,1)]

#     queue = deque([[start]])
#     visited = set()

#     while queue:
#         path = queue.popleft()
#         x, y = path[-1]

#         if (x,y) == end:
#             return path
    
#         for dx, dy in directions:
#             new_pos = (x + dx, y + dy)
#             if new_pos not in visited:
#                 visited.add(new_pos)
#                 new_path = path.copy()
#                 new_path.append(new_pos)
#                 queue.append(new_path)

#     return None

def bfs_shortest_path(start,end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])

def find_shortest_paths(galaxy_pairs):
    shortest_paths = {}
    print(len(galaxy_pairs))
    for idx, (start, end) in enumerate(galaxy_pairs):
        if idx % 10000 == 0: print(idx)
        shortest_path = bfs_shortest_path(start, end)
        shortest_paths[(start, end)] = shortest_path
    return shortest_paths

expanded_grid = expand_universe(grid)
positions_of_galaxies = find_galaxies(expanded_grid)
pairs = list(combinations(positions_of_galaxies, 2))
shortest_paths = find_shortest_paths(pairs)
# DEBUG
# for pair, path in shortest_paths.items():
#     print(f"Shortest path between {pair[0]} and {pair[1]} is: {path}")

print(f'{sum(path for path in shortest_paths.values()) }')

