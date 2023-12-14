import re
from itertools import cycle
from math import lcm
paths, *mappings = open('puzzle', 'r').read().split('\n')
mappings = dict(map(lambda x:(x[0:3],{"L": x[7:10],"R": x[-4:-1]}), mappings))
inf_paths = cycle(paths)

def count_step(step:str)->int:
    count = 0
    while re.match(r'\w\wZ', step) is None:
        choose = next(inf_paths)
        mapping = mappings[step]
        step = mapping[choose]
        count += 1
    return count 

start_steps =  dict(map(lambda x:(x,1),re.findall(r'\w\wA'," ".join(mappings.keys()))))
result = lcm(*[count_step(k) for k in start_steps.keys()])
print([count_step(k) for k in start_steps.keys()])