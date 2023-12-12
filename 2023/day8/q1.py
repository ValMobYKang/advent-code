from itertools import cycle
from functools import reduce
paths, *mappings = open('puzzle', 'r').read().split('\n')
mappings = dict(map(lambda x:(x[0:3],{"L": x[7:10],"R": x[-4:-1]}), mappings))
inf_paths = cycle(paths)

step = "AAA"
count = 0
while step != "ZZZ":
    choose = next(inf_paths)
    step = mappings[step][choose]
    count += 1
print(count)
