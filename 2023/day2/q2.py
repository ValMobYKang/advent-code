import re

VALID = {
"red": 12,
"green": 13,
"blue": 14
}
result = 0

with open('puzzle', 'r') as f:
    puzzle = f.readlines()

def str_to_int(strings:list[str]) -> list[int]:
    return [int(i) for i in strings]

def get_power(line:str):
    num_red = re.findall(pattern=r"(\d+) red",string=line)
    num_blue = re.findall(pattern=r"(\d+) blue",string=line)
    num_green = re.findall(pattern=r"(\d+) green",string=line)

    return max(str_to_int(num_red)) * max(str_to_int(num_green)) * max(str_to_int(num_blue))

for line in puzzle:
    result += get_power(line)

print(result)