import os, re

# https://adventofcode.com

word_to_num = {
    "one": '1',
    "two": "2",
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
 }

def get_func_from_gpt(line):
    calibration_value = 0
    pattern = '(?=(one|two|three|four|five|six|seven|eight|nine|1|2|3|4|5|6|7|8|9))'
    matches = [match.group(1) for match in re.finditer(pattern, line)]
    first = int(word_to_num.get(matches[0],matches[0]))
    second = int(word_to_num.get(matches[-1],matches[-1])) 
    return first * 10 + second

with open('./calibration', 'r') as f:
    total = 0
    for line in f.readlines():
        total += get_func_from_gpt(line.strip())

print(total)
