import re


def get_network(line: str) -> dict:
    match = re.match(r"(.*?) = \((.*?), (.*?)\)", line)
    key, val1, val2 = match.groups()

    return {key: (val1, val2)}


navigate = ""
networks = {}

with open("./data.txt", "r") as file:
    navigate = file.readline().strip()

    file.readline()  # skip a empty line
    for line in file:
        networks.update(get_network(line.strip()))

# print(navigate)
# print(networks)

next_node = "AAA"
FINISH = "ZZZ"

start_navigate = 0
NAVIGATE_SIZE = len(navigate) - 1

step = 0
while next_node != FINISH:
    step += 1

    route = 0 if navigate[start_navigate] == "L" else 1
    next_node = networks[next_node][route]

    if start_navigate == NAVIGATE_SIZE:
        start_navigate = 0
    else:
        start_navigate += 1

print(step)
