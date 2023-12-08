import re

numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

pattern = "\d|" + "|".join(numbers.keys())


def get_calibration_value(s: str) -> int:
    digits = re.findall(rf"{pattern}", s)

    # the file must always contain at least 1 digit
    return int(word_to_digit(digits[0]) + word_to_digit(digits[-1]))


def word_to_digit(digit: str) -> str:
    if digit in numbers:
        digit = digit.replace(digit, numbers[digit])

    return digit


calibration_values = []

with open("./data.txt", "r") as file1:
    for line in file1:
        calibration_values.append(get_calibration_value(line.strip()))

# print(calibration_values)
# print(len(calibration_values))

sum = 0

for num in calibration_values:
    sum += num

print(sum)
