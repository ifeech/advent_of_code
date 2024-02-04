import re
from math import lcm


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


def get_start_nodes() -> list:
    start_nodes = []
    for key in networks.keys():
        if key[-1] == "A":
            start_nodes.append(key)

    return start_nodes


def update_nodes_steps(nodes: list, nodes_steps: list, step: int):
    for key, node in enumerate(nodes):
        if node[-1] == "Z":
            nodes_steps[key] = step


def update_next_nodes(nodes: list, route: int):
    for key, node in enumerate(nodes):
        nodes[key] = networks[node][route]


def is_finish(nodes_steps: list) -> bool:
    for step in nodes_steps:
        if step == 0:
            return False

    return True


next_nodes = get_start_nodes()
nodes_steps = [0] * len(next_nodes)

start_navigate = 0
NAVIGATE_SIZE = len(navigate) - 1

step = 0
while not is_finish(nodes_steps):
    update_nodes_steps(next_nodes, nodes_steps, step)
    step += 1

    route = 0 if navigate[start_navigate] == "L" else 1
    update_next_nodes(next_nodes, route)

    if start_navigate == NAVIGATE_SIZE:
        start_navigate = 0
    else:
        start_navigate += 1

# print(nodes_steps)

print(lcm(*nodes_steps))
