import re
import math

colors = ["red", "green", "blue"]


def get_fewest_number_of_each_color(s: str) -> list:
    numbers = []

    for color in colors:
        revealed_cubes = re.findall(rf"(\d*) {color}", s)
        revealed_cubes_number = list(map(int, revealed_cubes))

        if revealed_cubes_number:
            numbers.append(max(revealed_cubes_number))

    return numbers


games = []

with open("./data.txt", "r") as file:
    for line in file:
        games.append(get_fewest_number_of_each_color(line.strip()))

# print(games)

power = 0

for game in games:
    power += math.prod(game)

print(power)
