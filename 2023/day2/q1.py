import os

VALID = {
    'red': 12,
    'green':13,
    'blue':14
}

result = 0
with open('puzzle', 'r') as f:
    puzzle = [item.strip() for item in f.readlines()]

def get_game_num(line):
    return int(line.split(':')[0].split(' ')[1])

def is_valid(line):
    for one in line.split(':')[1].split(';'):
        for num_color in one.split(','):
            num , color = num_color.strip().split(' ')
            if int(num) > VALID[color]: 
                print(line)
                print(num_color)
                return False
    return True

for line in puzzle:
    if is_valid(line): result += get_game_num(line)

print(result)