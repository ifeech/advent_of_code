def get_list_values(line: str) -> list:
    return [int(i) for i in line.split()]


def get_new_sequence(values: list) -> list:
    sequence = []

    for i, value in enumerate(values):
        if i == 0:
            prev_value = value
        else:
            new_value = value - prev_value
            sequence.append(new_value)
            prev_value = value

    return sequence


def get_prediction(values: list) -> int:
    if all(i == 0 for i in values):
        return values[0]

    return values[0] - get_prediction(get_new_sequence(values))


extrapolated_values = 0
with open("./data.txt", "r") as file:
    for line in file:
        values = get_list_values(line.strip())
        extrapolated_values += get_prediction(values)

print(extrapolated_values)
