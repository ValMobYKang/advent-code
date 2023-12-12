from itertools import combinations
from collections import deque
# Read the input grid from a text file
with open('puzzle', 'r') as file:
    puzzle = file.read()

grid = [list(row) for row in puzzle.splitlines()]

def expand_universe_and_get_new_positions(grid):
    # Parse the input into a list of lists (grid)
    rows = len(grid)
    cols = len(grid[0])

    # Determine which rows and columns are empty
    empty_rows = {i for i in range(rows) if all(grid[i][j] == '.' for j in range(cols))}
    empty_cols = {j for j in range(cols) if all(grid[i][j] == '.' for i in range(rows))}

    # Calculate the new positions of the galaxies
    new_positions = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                # Calculate new position
                new_i = i + (1000000 - 1) * len([r for r in empty_rows if r < i])
                new_j = j + (1000000 - 1) * len([c for c in empty_cols if c < j])
                new_positions.append((new_i, new_j))

    return new_positions

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

new_positions = expand_universe_and_get_new_positions(grid)
pairs = list(combinations(new_positions, 2))
shortest_paths = find_shortest_paths(pairs)
# DEBUG
# for pair, path in shortest_paths.items():
#     print(f"Shortest path between {pair[0]} and {pair[1]} is: {path}")

print(f'{sum(path for path in shortest_paths.values()) }')

