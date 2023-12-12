with open('puzzle' ,'r') as f:
    puzzle = f.read()

puzzle = [list(map(int, line.split(' '))) for line in puzzle.split('\n')]

def next_level(cache, level):
    if not any(level): return
    cache.insert(0,level)
    temp = [(level[i] - level[i-1]) for i in range(1,len(level))]
    next_level(cache, temp)
    return cache

def get_pred(line):
    sequences = next_level(cache=[], level=line)
    pred = 0
    for i in sequences:
        pred = i[-1] + pred
    return pred


print(sum([get_pred(line) for line in puzzle]))
