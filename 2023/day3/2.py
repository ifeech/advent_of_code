from functools import reduce

GEAR_SYMBOL = "*"


def get_numbers_and_symbols_positions(s: str) -> dict:
    numbers = []
    symbols = []

    number = ""
    number_position = []

    for index, char in enumerate(s):
        if char.isdigit():
            # forming a number by digit
            number += char
            number_position.append(index)
        elif number.isdigit():
            # saving the generated number when the current character is not a digit
            numbers.append((number, number_position[0], number_position[-1]))

            number = ""
            number_position = []

        if char == GEAR_SYMBOL:
            symbols.append((char, index, index))

    # if the number is at the end of the string
    if number.isdigit():
        numbers.append((number, number_position[0], number_position[-1]))

    return {
        "numbers": numbers,
        "symbols": symbols,
    }


def get_near_numbers(numbers: list, position_start: int, position_end: int) -> list:
    gear_numbers = []

    for number in numbers:
        if (number[1] >= position_start and number[1] <= position_end) or (
            number[2] >= position_start and number[2] <= position_end
        ):
            gear_numbers.append(int(number[0]))

    return gear_numbers


engine_schematic_positions = []

with open("./data.txt", "r") as file:
    for line in file:
        engine_schematic_positions.append(
            get_numbers_and_symbols_positions(line.strip())
        )

# print(engine_schematic_positions)

numbers_adjacent_to_a_symbol = []

for index, positions in enumerate(engine_schematic_positions):
    # lines on which to check for contact between the number and the symbol
    checked_lines = (index - 1, index, index + 1)

    for symbol in positions["symbols"]:
        gear_numbers = []

        # character search positions given the diagonal
        position_start = symbol[1] - 1 if symbol[1] > 0 else symbol[1]
        position_end = symbol[2] + 1

        # line-by-line inspection
        for line in checked_lines:
            if line < 0 or line >= len(engine_schematic_positions):
                continue

            gear_numbers += get_near_numbers(
                engine_schematic_positions[line]["numbers"],
                position_start,
                position_end,
            )

        if len(gear_numbers) == 2:
            numbers_adjacent_to_a_symbol.append(tuple(gear_numbers))

# print(numbers_adjacent_to_a_symbol)

gear_ratio = 0

for gear_numbers in numbers_adjacent_to_a_symbol:
    gear_ratio += gear_numbers[0] * gear_numbers[1]


print(gear_ratio)
