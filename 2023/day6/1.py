import re


def parse_line(line: str) -> list:
    return map(int, re.findall(r"(\d+)", line))


races = []
with open("./data.txt", "r") as file:
    lines = file.readlines()

    time = parse_line(lines[0])
    distance = parse_line(lines[1])

    races = list(zip(time, distance))

# print(races)


def get_winning_range_for_distance(time: int, distance: int) -> tuple:
    i = 1
    while i < time:
        if i * (time - i) > distance:
            break

        i += 1

    return (i, time - i)


winning_ranges_of_button_holding = []
for race in races:
    winning_ranges_of_button_holding.append(get_winning_range_for_distance(*race))

# print(winning_ranges_of_button_holding)

number_of_ways_to_beat_record = 1  # for simplicity
for winning_range in winning_ranges_of_button_holding:
    number_of_ways_to_beat_record *= winning_range[1] - winning_range[0] + 1

print(number_of_ways_to_beat_record)
