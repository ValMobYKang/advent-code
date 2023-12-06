import re

with open('puzzle', 'r') as f:
    puzzle = f.readlines()
puzzle_map = []
for y in puzzle:
    row = [x for x in y]
    for x in y:
        row.append(x)
    puzzle_map.append(row)

symbol_pos = []
num_range = []
for row, line in enumerate(puzzle):
    matches = re.finditer(r'[^0-9\.]', line.strip())

    for match in matches:
        symbol_pos.append((row, match.start()))

for row, line in enumerate(puzzle):
    matches = re.finditer(r'\d+', line.strip())

    for match in matches:
        num_range.append((match.group(), row, match.span()))

total = 0
for sym_y, sym_x in symbol_pos:
    for num, dig_y, dig_span in num_range:
        dig_start = dig_span[0]
        dig_end = dig_span[1]-1

        dy = abs(sym_y - dig_y) < 2
        dx_start = abs(sym_x - dig_start) < 2
        dx_end   = abs(sym_x - dig_end) < 2
        if ( dy and dx_start) or (dy and dx_end):
            print(f'{num}:[{dig_y},{dig_start}] <-> sym:[{sym_y,sym_x}]')
            total += int(num)

print(total)