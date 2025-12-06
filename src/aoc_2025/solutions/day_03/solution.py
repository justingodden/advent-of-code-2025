from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read().splitlines()

with open(_dir / "input.txt") as file:
    data = file.read().splitlines()


def part_1(data: list[str]):
    total = 0
    for bank in data:
        nums = [int(c) for c in bank[:-1]]
        l = sorted(nums)[-1]
        for i, c in enumerate(bank):
            if c == str(l):
                idx = i
                break
        nums = [int(c) for c in bank[idx + 1 :]]
        r = sorted(nums)[-1]
        total += int(str(l) + str(r))
    return total


def part_2(data: list[str]):
    total = 0
    for bank in data:
        i = 0
        bank = [int(c) for c in bank]
        prev_len = len(bank)
        while True:
            if len(bank) == 12:
                break
            if bank[i] < bank[i + 1]:
                bank.pop(i)
                i = 0
            else:
                i += 1
            if i == len(bank) - 1:
                if prev_len == len(bank):
                    break
                i = 0
                prev_len = len(bank)
        bank = "".join([str(c) for c in bank])
        bank = bank[:12]
        total += int(bank)
    return total


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))
