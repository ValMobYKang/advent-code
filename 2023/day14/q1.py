p = print

with open('puzzle', 'r') as f:
    puzzle = f.read()

one = list(map(list,zip(*puzzle.strip().split('\n'))))

def get_cal(line, i):
    """
    # >>> get_cal(line=['O', 'O', '.', 'O', '.', 'O', '.', '.', '#', '#'],i=3)
    # ['O', 'O', 'O', '.', '.', 'O', '.', '.', '#', '#']
    >>> get_cal(line=['#', '.', '#', '.', '.', 'O', '#', '.', '#', '#'], i=5)
    ['#', '.', '#', 'O', '.', '.', '#', '.', '#', '#']
    """
    ret_line = line.copy()
    while i - 1 > 0 and line[i-1] == '.':
        ret_line[i-1], ret_line[i] = ret_line[i], ret_line[i-1]
        i-=1
    if i == 1 and line[i-1] == '.':
        ret_line[i-1], ret_line[i] = ret_line[i], ret_line[i-1]
    return ret_line

def get_line_score(line):
    """
    >>> get_line_score(line=['O', 'O', 'O', 'O', '.', '.', '.', '.', '#', '#'])
    34
    """
    score = 0
    total = len(line)
    i = 0
    while i < total:
        if line[i] == 'O':
            score += (total-i)
        i+=1
    return score

score = 0
for row in one:
    temp_row = row.copy()
    for idx in range(len(row)):
        if row[idx] == '#': continue
        temp_row = get_cal(temp_row, idx)
    score += get_line_score(temp_row)
print(score)