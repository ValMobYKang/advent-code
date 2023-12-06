# self-defined
with open('puzzle', 'r') as f:
    raw_puzzle = f.readlines()
    puzzle, temp_map = [], []
    for line in raw_puzzle:
        if line == '\n':
            puzzle.append(temp_map)
            temp_map = []
            continue
        temp_map.append(line.strip())
    puzzle.append(temp_map)

def return_map(one_map:list[str]):
    result = []
    for idx, line in enumerate(one_map):
        if idx == 0: continue
        result.append(tuple([int(num) for num in line.split(' ')]))
    return result

seeds = puzzle[0][0].strip().split(' ')[1:]
seed_to_soil_map = return_map(puzzle[1])
soil_to_fertilizer_map = return_map(puzzle[2])
fertilizer_to_water_map = return_map(puzzle[3])
water_to_light_map = return_map(puzzle[4])
light_to_temperature_map = return_map(puzzle[5])
temperature_to_humidity_map = return_map(puzzle[6])
humidity_to_location_map = return_map(puzzle[7])

seed_ranges = []
for idx in range(len(seeds))[::2]:
    seed_ranges.append((int(seeds[idx]), int(seeds[idx+1])))


## GPT-4
def map_number(number, map_list):
    for destination_start, source_start, length in map_list:
        if source_start <= number < source_start + length:
            return destination_start + (number - source_start)
    return number

# Redefine map_number to operate on ranges
def map_range(start, length, map_list):
    min_location = float('inf')
    for i in range(start, start + length):
        mapped = i
        for mapping in map_list:
            mapped = map_number(mapped, mapping)
        min_location = min(min_location, mapped)
        # Short-circuit if we hit the start of any range in the final map
        for destination_start, _, _ in humidity_to_location_map:
            if min_location == destination_start:
                return min_location
    print(min_location)
    return min_location

# Define the sequence of maps as a list
maps_sequence = [
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map
]

# Find the lowest location number for each range and then take the minimum
lowest_location = min(map_range(start, length, maps_sequence) for start, length in seed_ranges)

# Only the line that computes the lowest_location is changed
print("The lowest location number is:", lowest_location)