from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read().splitlines()

with open(_dir / "input.txt") as file:
    data = file.read().splitlines()


def part_1(data: list[str]):
    ids = data[0].split(",")
    invalid = 0

    for _id in ids:
        low, high = _id.split("-")
        low = int(low)
        high = int(high)
        nums = range(low, high + 1)
        for num in nums:
            s = str(num)
            if s[: len(s) // 2] == s[len(s) // 2 :]:
                invalid += num
    return invalid


def part_2(data: list[str]):
    ids = data[0].split(",")
    invalid = 0

    for _id in ids:
        low, high = _id.split("-")
        low = int(low)
        high = int(high)
        nums = range(low, high + 1)
        for num in nums:
            s = str(num)
            for step in range(1, len(s) // 2 + 1):
                tmp_set = set[int]()
                for i in range(0, len(s), step):
                    tmp = int(s[i : i + step])
                    tmp_set.add(tmp)
                if len(tmp_set) == 1:
                    invalid += num
                    break
    return invalid


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))
