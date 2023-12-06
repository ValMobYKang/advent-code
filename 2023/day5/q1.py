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


## GPT-3.5
def convert_number(number, mappings):
    number = int(number)
    for destination_start, source_start, length in mappings:
        if number >= source_start and number < source_start + length:
            return destination_start + (number - source_start)
    return number

# Convert seed numbers to soil numbers
soil_numbers = [convert_number(seed, seed_to_soil_map) for seed in seeds]

# Convert soil numbers to fertilizer numbers
fertilizer_numbers = [convert_number(soil, soil_to_fertilizer_map) for soil in soil_numbers]

# Convert fertilizer numbers to water numbers
water_numbers = [convert_number(fertilizer, fertilizer_to_water_map) for fertilizer in fertilizer_numbers]

# Convert water numbers to light numbers
light_numbers = [convert_number(water, water_to_light_map) for water in water_numbers]

# Convert light numbers to temperature numbers
temperature_numbers = [convert_number(light, light_to_temperature_map) for light in light_numbers]

# Convert temperature numbers to humidity numbers
humidity_numbers = [convert_number(temperature, temperature_to_humidity_map) for temperature in temperature_numbers]

# Convert humidity numbers to location numbers
location_numbers = [convert_number(humidity, humidity_to_location_map) for humidity in humidity_numbers]

# Find the lowest location number
lowest_location_number = min(location_numbers)

print("Lowest location number:", lowest_location_number)

## GPT-4
# Process each seed through the maps
locations = []
for seed in seeds:
    soil = convert_number(seed, seed_to_soil_map)
    fertilizer = convert_number(soil, soil_to_fertilizer_map)
    water = convert_number(fertilizer, fertilizer_to_water_map)
    light = convert_number(water, water_to_light_map)
    temperature = convert_number(light, light_to_temperature_map)
    humidity = convert_number(temperature, temperature_to_humidity_map)
    location = convert_number(humidity, humidity_to_location_map)
    locations.append(location)

# Find the lowest location number
lowest_location = min(locations)
print("The lowest location number is:", lowest_location)