with open('puzzle' ,'r') as f:
    puzzle = f.read()

puzzle = [list(map(int, line.split(' '))) for line in puzzle.split('\n')]
def next_level(cache, level):
    if not any(level):
        return
    cache.insert(0,level)
    temp = [(level[i] - level[i-1]) for i in range(1,len(level))]
    next_level(cache, temp)
    return cache

def get_prev(line):
    prev = 0
    sequences = next_level(cache=[],level=line)
    for i in sequences:
        prev = i[0] - prev
    return prev

print(sum([get_prev(line) for line in puzzle]))