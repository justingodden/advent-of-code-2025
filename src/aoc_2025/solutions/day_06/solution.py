import math
import re
from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read().splitlines()

with open(_dir / "input.txt") as file:
    data = file.read().splitlines()


def part_1(data: list[str]):
    ops = data[-1].replace(" ", "")
    data = data[:-1]
    for i, row in enumerate(data):
        row = re.sub(r" +", " ", row)
        row = row.strip()
        row = [int(c) for c in row.split(" ")]
        data[i] = row

    data = list(zip(*data))
    total = 0
    for i, row in enumerate(data):
        if ops[i] == "+":
            total += sum(row)
        else:
            total += math.prod(row)

    return total


def part_2(data: list[str]):
    ops = data[-1].replace(" ", "")
    data = data[:-1]
    data = [[c for c in row] for row in data]
    data = list(zip(*data))
    data = ["".join(row) for row in data]
    data = [s.replace(" ", "") for s in data]
    data = [int(s) if s else None for s in data]
    idx = 0
    total = 0
    for op in ops:
        tmp = []
        for i, s in enumerate[int](data[idx:], idx):
            if s is None:
                idx = i + 1
                break
            tmp.append(s)
        if op == "+":
            total += sum(tmp)
        else:
            total += math.prod(tmp)
    return total


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))
