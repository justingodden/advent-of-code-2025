from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read()

with open(_dir / "input.txt") as file:
    data = file.read()


def part_1(data: str):
    total = 0
    fresh_ranges, ids = data.split("\n\n")
    fresh_ranges = fresh_ranges.split("\n")
    ids = ids.split("\n")
    for _id in ids:
        _id = int(_id)
        for fresh_range in fresh_ranges:
            low, high = fresh_range.split("-")
            low = int(low)
            high = int(high)
            if _id >= low and _id <= high:
                total += 1
                break
    return total


def part_2(data: str):
    data = data.split("\n\n")[0]
    data = data.split("\n")
    data = [[int(c) for c in d.split("-")] for d in data]
    data = sorted(data, key=lambda x: x[0])

    total = 0
    last = None

    for low, high in data:
        if last is None:
            last = [low, high]

        elif low > last[1]:
            total += last[1] - last[0] + 1
            last = [low, high]

        else:
            last[1] = max(last[1], high)

    total += last[1] - last[0] + 1
    return total


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))
