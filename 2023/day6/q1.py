
times = [44,82,69,81]
distances = [202, 1076, 1138, 1458]

def calculate_ways(time, distance):
    ways = 0
    for hold_time in range(time):
        speed = hold_time
        travel_time = time - hold_time
        if speed * travel_time > distance:
            ways += 1
    return ways


ways_to_win = [calculate_ways(time, distance) for time, distance in zip(times, distances)]

result = 1
for ways in ways_to_win:
    result *= ways

print(result)