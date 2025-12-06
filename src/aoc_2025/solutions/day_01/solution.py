from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read().splitlines()

with open(_dir / "input.txt") as file:
    data = file.read().splitlines()


def part_1(data: list[str]):
    pos = 50
    code = 0

    for instruction in data:
        direction = instruction[0]
        val = int(instruction[1:])
        if direction == "R":
            tmp_pos = pos + val
            if pos + val > 99:
                tmp_pos %= 100
            pos = tmp_pos
        else:
            tmp_pos = pos - val
            if pos - val < 0:
                tmp_pos %= 100
            pos = tmp_pos
        if pos == 0:
            code += 1
    return code


def part_2(data: list[str]):
    pos = 50
    code = 0
    for instruction in data:
        direction = instruction[0]
        val = int(instruction[1:])
        if direction == "R":
            code += (pos + val) // 100
            pos = (pos + val) % 100
        else:
            if pos == 0:
                code += val // 100
            elif val == pos:
                code += 1
            elif val > pos:
                code += 1 + (val - pos) // 100
            pos = (pos - val) % 100

    return code


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))


if __name__ == "__main__":
    solve()
