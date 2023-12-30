class NumbersToConvert:
    def __init__(self, source_start: int, destination_start: int, length: int) -> None:
        self.source_start = source_start
        self.destination_start = destination_start
        self.length = length

    def in_source_range(self, source: int) -> bool:
        return source >= self.source_start and source <= self._get_source_end()

    def get_destination(self, source: int) -> int:
        return self.destination_start + (source - self.source_start)

    def _get_source_end(self) -> int:
        return self.source_start + self.length - 1


def parse_range(line: str) -> NumbersToConvert:
    numbers = line.split()

    return NumbersToConvert(int(numbers[1]), int(numbers[0]), int(numbers[2]))


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
almanac_ranges = {}
destination_key = ""

with open("./data.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line == "":
            continue

        line_split = line.split()
        if line_split:
            if line_split[0] == "seeds:":
                seeds = line_split[1:]

            if MAP_TYPES.get(line_split[0]):
                destination_key = MAP_TYPES[line_split[0]]
                almanac_ranges[destination_key] = []

                continue

            if not destination_key:
                continue

            almanac_ranges[destination_key].append(parse_range(line))

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


def get_next_destination(step: int, source: int) -> int:
    type = STEPS[step]

    # Any source numbers that aren't mapped correspond to the same destination number.
    # So, seed number 10 corresponds to soil number 10.
    destination = source

    for range in almanac_ranges[type]:
        if range.in_source_range(source):
            destination = range.get_destination(source)

            break

    # find the location number
    if type == "location":
        return destination

    return get_next_destination(step + 1, destination)


min_destination = None

for seed in seeds:
    destination = get_next_destination(0, int(seed))

    if not min_destination or min_destination > destination:
        min_destination = destination

print(min_destination)