import re, os

total = 0
with open("puzzle", 'r') as f:
    puzzle = f.readlines()

def get_score(times:int) -> int:
    """
    >>> get_score(1)
    1
    >>> get_score(3)
    4
    """
    if times == 0: raise Exception("input should not be 0.")
    score, times = 1, times -1
    if times == 0: return score
    for _ in range(times):
        score *= 2
    return score

for idx, line in enumerate(puzzle):
    left_right = line.strip().split(': ')[-1]
    left, right = left_right.split(' | ')
    result = set(left.split(' ')) & set(right.split(' '))
    
    if '' in result: result.remove('')
    
    if not result: continue
    print(idx, result)
    total += get_score(len(result))

print(total)