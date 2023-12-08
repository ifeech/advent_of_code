import re


def get_calibration_value(s: str) -> int:
    digit1 = get_digit(s)
    digit2 = get_digit(s[::-1])

    return int(digit1 + digit2)


def get_digit(s: str) -> str:
    # the file must always contain at least 1 digit
    n = re.search("\d", s)

    return n[0]


calibration_values = []

with open("./data.txt", "r") as file:
    for line in file:
        calibration_values.append(get_calibration_value(line.strip()))

sum = 0

for num in calibration_values:
    sum += num

print(sum)
