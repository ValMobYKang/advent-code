from collections import deque

with open('puzzle','r') as f:
    raw = f.readlines()
    puzzle = []
    for line in raw:
        first = line.split(' ')[0]
        second = list(map(int, line.strip().split(' ')[1].split(',')))
        puzzle.append([first, second])

def match_list_heads(list1, list2):
    min_length = min(len(list1), len(list2))
    for i in range(min_length):
        if list1[i] != list2[i]:
            return False
            
    return True

def str2list(combine):
   return [len(i) for i in combine.split('.') if i != ''] 

def get_all_combines(s, block):
    count = 0
    queue = deque([s])

    while queue:
        current_str = queue.popleft()
        q_mark_index = current_str.find("?")

        if q_mark_index != -1 and current_str[:q_mark_index].endswith('.') and not match_list_heads(str2list(current_str[:q_mark_index]),block): 
                continue
        if q_mark_index == -1:
            if str2list(current_str) == block: count += 1
        else:
            new_dot_str = current_str[:q_mark_index] + '.' + current_str[q_mark_index+1:]
            if match_list_heads(str2list(new_dot_str[:q_mark_index+1]),block): 
                queue.append(new_dot_str)

            new_s_str = current_str[:q_mark_index] + '#' + current_str[q_mark_index+1:]
            queue.append(new_s_str)

    return count

total = 0 
for idx,(first, block) in enumerate(puzzle):
    total += get_all_combines(first,block)
    
print(total)
