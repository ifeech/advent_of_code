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
        "quantity": 1,
    }


def count_cards(scratchcards_statistics: list):
    for index, card in enumerate(scratchcards_statistics):
        number_of_winning_numbers = get_number_of_winning_numbers(card)
        for n in range(number_of_winning_numbers):
            scratchcards_statistics[index + 1 + n]["quantity"] += card["quantity"]


def get_number_of_winning_numbers(card: list) -> int:
    number_of_winning_numbers = 0

    for number in card["numbers"]:
        if number in card["winning_numbers"]:
            number_of_winning_numbers += 1

    return number_of_winning_numbers


scratchcards_statistics = []

with open("./data.txt", "r") as file:
    for line in file:
        scratchcards_statistics.append(parse_card_points(line.strip()))

# print(scratchcards_statistics)

count_cards(scratchcards_statistics)

card_quantity = 0

for card in scratchcards_statistics:
    card_quantity += card["quantity"]

print(card_quantity)
