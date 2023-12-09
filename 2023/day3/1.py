SERVICE_SYMBOL = "."


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

        if not char.isdigit() and char != SERVICE_SYMBOL:
            symbols.append((char, index, index))

    # if the number is at the end of the string
    if number.isdigit():
        numbers.append((number, number_position[0], number_position[-1]))

    return {
        "numbers": numbers,
        "symbols": symbols,
    }


def check_near_symbol(symbols: list, position_start: int, position_end: int) -> bool:
    for symbol in symbols:
        if position_start <= symbol[1] and position_end >= symbol[2]:
            return True

    return False


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

    for number in positions["numbers"]:
        # character search positions given the diagonal
        position_start = number[1] - 1 if number[1] > 0 else number[1]
        position_end = number[2] + 1

        # line-by-line inspection
        for line in checked_lines:
            if line < 0 or line >= len(engine_schematic_positions):
                continue

            if check_near_symbol(
                engine_schematic_positions[line]["symbols"],
                position_start,
                position_end,
            ):
                numbers_adjacent_to_a_symbol.append(int(number[0]))

                # forced termination of the check
                # at the first confirmation of finding a character next to a number
                break

# print(numbers_adjacent_to_a_symbol)

sum = 0

for numbers in numbers_adjacent_to_a_symbol:
    sum += numbers

print(sum)
