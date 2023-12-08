import re

RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

colors = {
    "red": RED_CUBES,
    "green": GREEN_CUBES,
    "blue": BLUE_CUBES,
}


def check_game(s: str) -> bool:
    for color, cubes in colors.items():
        revealed_cubes = re.findall(rf"(\d*) {color}", s)
        revealed_cubes_number = list(map(int, revealed_cubes))

        if revealed_cubes_number and max(revealed_cubes_number) > cubes:
            return False

    return True


i = 1
results = []

with open("./data.txt", "r") as file:
    for line in file:
        results.append((i, check_game(line.strip())))
        i += 1

# print(results)

sum = 0

for id, status in results:
    if status:
        sum += id

print(sum)
