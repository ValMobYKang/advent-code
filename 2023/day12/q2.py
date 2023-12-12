from functools import cache


@cache
def foo(s, block):
    # start from '#' or '?'
    s = s.lstrip('.')

    # If s or block are done
    if s == '':
        # matched 
        return int(block == ())

    if block == ():
        # should not find more #
        return int(s.find('#') == -1)
    
    # if start from '#'
    if s[0] == '#':
        if len(s) < block[0] or '.' in s[:block[0]]:
            return 0
        elif len(s) == block[0]:
            return int(len(block) == 1) 
        elif s[block[0]] == '#':
            return 0
        else:
            # print(f"=> {s[block[0]+1:]}")
            return foo(s[block[0]+1:], block[1:]) # next

    # if start from '?'
    # print(f"-> {'#'+s[1:]}")
    return foo('#'+s[1:], block) + foo(s[1:], block)


puzzle = [c.strip().split() for c in open('puzzle').readlines()]
puzzle = [[c[0], tuple(map(int, c[1].strip().split(',')))] for c in puzzle]
puzzle = [[ (s[0] + '?') * 4 + s[0], s[1]*5] for s in puzzle]

for [s, block] in puzzle:
    foo(s,block)


