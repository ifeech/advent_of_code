from collections import Counter
import functools


def parse_poker_hand(line: str) -> tuple:
    puzzle = line.split(" ")
    hand = puzzle[0]
    bid = int(puzzle[1])

    return (hand, bid)


POKER_HANDS_TYPE_FIVE = "five"
POKER_HANDS_TYPE_FOUR = "four"
POKER_HANDS_TYPE_FULL_HOUSE = "full_house"
POKER_HANDS_TYPE_THREE = "three"
POKER_HANDS_TYPE_TWO = "two"
POKER_HANDS_TYPE_ONE = "one"
POKER_HANDS_TYPE_HIGH_CARD = "hight_card"

POKER_HANDS_TYPES = {
    POKER_HANDS_TYPE_HIGH_CARD: [],
    POKER_HANDS_TYPE_ONE: [],
    POKER_HANDS_TYPE_TWO: [],
    POKER_HANDS_TYPE_THREE: [],
    POKER_HANDS_TYPE_FULL_HOUSE: [],
    POKER_HANDS_TYPE_FOUR: [],
    POKER_HANDS_TYPE_FIVE: [],
}


def categorize_poker_hand(poker_hand: type):
    hand = poker_hand[0]
    type = identify_hand_type(hand)

    POKER_HANDS_TYPES[type].append(poker_hand)


def get_max_symbols_count_with_J(hand: str):
    symbols_count = Counter(hand)

    if symbols_count.get("J"):
        jokers_counts = symbols_count.pop("J")
    else:
        jokers_counts = 0

    return max(symbols_count.values()) + jokers_counts


def identify_hand_type(hand: str) -> str:
    unique_cards = set(hand) - set("J")  # "J" will become another char
    len_unique_cards = len(unique_cards)

    if len_unique_cards == 1 or len_unique_cards == 0:
        return POKER_HANDS_TYPE_FIVE

    if len_unique_cards == 5:
        return POKER_HANDS_TYPE_HIGH_CARD

    if len_unique_cards == 4:
        return POKER_HANDS_TYPE_ONE

    max_symbols_count = get_max_symbols_count_with_J(hand)

    if len_unique_cards == 2:
        if max_symbols_count == 4:
            return POKER_HANDS_TYPE_FOUR
        else:
            return POKER_HANDS_TYPE_FULL_HOUSE

    if max_symbols_count == 3:
        return POKER_HANDS_TYPE_THREE

    return POKER_HANDS_TYPE_TWO


with open("./data.txt", "r") as file:
    for line in file:
        poker_hand = parse_poker_hand(line)
        categorize_poker_hand(poker_hand)

# print(POKER_HANDS_TYPES)

TOTAL = 0
RANK = 1

CARD_RATING = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def sort_hands(poker_hand_1: tuple, poker_hand_2: tuple) -> list:
    hand_1 = poker_hand_1[0]
    hand_2 = poker_hand_2[0]

    if hand_1 == hand_2:
        return 0

    for k, char in enumerate(hand_1):
        hand_1_rating = CARD_RATING.index(char)
        hand_2_rating = CARD_RATING.index(hand_2[k])

        if hand_1_rating == hand_2_rating:
            continue

        if hand_1_rating > hand_2_rating:
            return 1

        return -1


for poker_hands in POKER_HANDS_TYPES.values():
    if poker_hands:
        sorted_poker_hands = sorted(poker_hands, key=functools.cmp_to_key(sort_hands))

        for hand, bid in sorted_poker_hands:
            TOTAL += bid * RANK
            RANK += 1

print(TOTAL)
