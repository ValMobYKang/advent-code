with open('puzzle', 'r') as f:
    puzzle = f.read().split('\n\n')

def transpose(x):
	return list(map(list, zip(*x)))

def match_one_diff(left, right):
    flag = True
    for i in range(min(len(left),len(right))):
        if left[i] == right[i]:
            continue
        elif left[i] != right[i] and flag:
            flag = False
            continue
        elif left[i] != right[i] and not flag:
            return False
    return True

def find_mirror_index(pattern):
    for i in range(len(pattern)-1):
        left = "".join(j for j in pattern[:i+1][::-1])
        right = "".join(j for j in pattern[i+1:])

        is_perfect_mirror = right.startswith(left) if len(left) < len(right) else left.startswith(right)
        if is_perfect_mirror: continue
        if match_one_diff(left,right): return i+1 
    return 0

total = 0
for patterns in puzzle:
    horizontal = patterns.split('\n')

    vertical = []
    for i in range(len(horizontal[0])):
        vertical.append("".join(row[i] for row in horizontal))
    
    total += (find_mirror_index(vertical) + find_mirror_index(horizontal)*100)
    # break
    # print(find_mirror_index(vertical),find_mirror_index(horizontal))
    
    
print(total)