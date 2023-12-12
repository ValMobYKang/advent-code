import sys
sys.setrecursionlimit(100000)


with open('puzzle','r') as f:
    puzzle = f.readlines()
    SKETCH = [[char for char in line.strip()] for line in puzzle]

NUM_ROW, NUM_COL = len(SKETCH), len(SKETCH[0])

# Find S Position
def get_start() -> tuple[int,int]:
    point_s = None
    for i in range(NUM_ROW):
        for j in range(NUM_COL):
            if SKETCH[i][j] == "S":
                point_s = (i,j)
    return point_s

DIRECTION = {
    'up': ['J','|','L','S'],
    'down': ['|','7','F','S'],
    'left': ['7','-','J','S'],
    'right': ['-','F','L','S']
}

# Get Round Position
def get_next(point: tuple[int, int]):
    row, col = point
    next_points = []
    symbol = SKETCH[row][col] # 7

    # up
    if row > 0 and symbol in DIRECTION['up']:
        next_points.append((row-1, col))
   
    # down
    if row + 1 < NUM_ROW and symbol in DIRECTION['down']:
        next_points.append((row+1, col))

    # left
    if col > 0 and symbol in DIRECTION['left']:
        next_points.append((row, col-1))

    # right
    if col + 1 < NUM_COL and symbol in DIRECTION['right']:
        next_points.append((row, col+1))

    return next_points

def find_path(point, pipe=[]):
    if point in pipe: return
    pipe.append(point)
    for next_p in get_next(point):
        if SKETCH[next_p[0]][next_p[1]] == '.':continue
        # print(f"{SKETCH[point[0]][point[1]]} {point} -> {SKETCH[next_p[0]][next_p[1]]} {next_p}")
        find_path(next_p,pipe)
    return pipe

print(f"{SKETCH[2][0]} -> {get_next((2,0))}")
print(len(find_path(get_start()))/2)
