import re


def parse_card_points(s: str) -> dict:
    try:
        colon_position = s.index(":")
    except ValueError:
        colon_position = 0

    try:
        separator_position = s.index("|")
    except ValueError:
        separator_position = 0

    return {
        "winning_numbers": re.findall(r"(\d+)", s[colon_position:separator_position]),
        "numbers": re.findall(r"(\d+)", s[separator_position:]),
    }


scratchcards_statistics = []

with open("./data.txt", "r") as file:
    for line in file:
        scratchcards_statistics.append(parse_card_points(line.strip()))

# print(scratchcards_statistics)


def get_number_of_winning_numbers(card: list) -> int:
    number_of_winning_numbers = 0

    for number in card["numbers"]:
        if number in card["winning_numbers"]:
            number_of_winning_numbers += 1

    return number_of_winning_numbers


points = 0

for card in scratchcards_statistics:
    number_of_winning_numbers = get_number_of_winning_numbers(card)
    if number_of_winning_numbers:
        points += 2 ** (number_of_winning_numbers - 1)

print(points)
