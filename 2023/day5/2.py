class NumbersToConvert:
    def __init__(self, source_start: int, destination_start: int, length: int) -> None:
        self.source_start = source_start
        self.destination_start = destination_start
        self.length = length

    def not_in_source_range(self, source: tuple) -> bool:
        return source[0] > self.get_source_end() or source[1] < self.source_start

    def get_source_end(self) -> int:
        return self.source_start + self.length

    def get_destination_range(self, source_start: int, source_end: int) -> tuple:
        destination_start = self.destination_start + (source_start - self.source_start)
        destination_end = self.destination_start + (source_end - self.source_start)

        return (destination_start, destination_end)


def parse_range(line: str) -> NumbersToConvert:
    numbers = line.split()

    return NumbersToConvert(int(numbers[1]), int(numbers[0]), int(numbers[2]))


def parse_seeds(line_split: list) -> list:
    seeds = []

    for i in range(0, len(line_split) - 1, 2):
        start_seeds_range = int(line_split[i])
        length_range = int(line_split[i + 1])
        seeds.append((start_seeds_range, start_seeds_range + length_range - 1))

    return seeds


MAP_TYPES = {
    "seed-to-soil": "soil",
    "soil-to-fertilizer": "fertilizer",
    "fertilizer-to-water": "water",
    "water-to-light": "light",
    "light-to-temperature": "temperature",
    "temperature-to-humidity": "humidity",
    "humidity-to-location": "location",
}

seeds = []
ranges = {}
destination_key = ""

with open("./data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        line_split = line.split()
        if line_split:
            if line_split[0] == "seeds:":
                seeds = parse_seeds(line_split[1:])

            if MAP_TYPES.get(line_split[0]):
                destination_key = MAP_TYPES[line_split[0]]
                ranges[destination_key] = []

                continue

            if not destination_key:
                continue

            ranges[destination_key].append(parse_range(line))

# find the lowest location number that corresponds to any of the initial seeds.

STEPS = (
    "soil",
    "fertilizer",
    "water",
    "light",
    "temperature",
    "humidity",
    "location",
)

min_destinations = []


def get_next_destination(step: int, source_ranges: list):
    type = STEPS[step]

    source_ranges_copy = source_ranges

    i = 0
    while i < len(source_ranges_copy):
        source_range = source_ranges_copy[i]
        i += 1

        destination_ranges = []

        for range in ranges[type]:
            if range.not_in_source_range(source_range):
                continue

            source_start = max(source_range[0], range.source_start)
            source_end = min(source_range[1], range.get_source_end())

            destination_ranges.append(
                range.get_destination_range(source_start, source_end)
            )

            if source_range[0] < source_start:
                source_ranges_copy.append((source_range[0], source_start - 1))

            if source_range[1] > source_end:
                source_ranges_copy.append((source_end + 1, source_range[1]))

        # Any source numbers that aren't mapped correspond to the same destination number.
        if not destination_ranges:
            destination_ranges = [source_range]

        # find the location number
        if type == "location":
            min_destinations.append(destination_ranges[0][0])
        else:
            get_next_destination(step + 1, destination_ranges)


get_next_destination(0, seeds)

print(min(min_destinations))