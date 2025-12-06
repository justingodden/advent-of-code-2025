from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read().splitlines()

with open(_dir / "input.txt") as file:
    data = file.read().splitlines()


def get_neighbors(j: int, i: int) -> list[tuple[int, int]]:
    return [
        (j - 1, i - 1),
        (j - 1, i),
        (j - 1, i + 1),
        (j, i - 1),
        (j, i + 1),
        (j + 1, i - 1),
        (j + 1, i),
        (j + 1, i + 1),
    ]


def print_data(data: list[str], j: int, i: int):
    tmp_data = data.copy()
    tmp_data[j] = tmp_data[j][:i] + "X" + tmp_data[j][i + 1 :]
    for line in tmp_data:
        print(line)


def part_1(data: list[str]):
    total = 0
    for j in range(len(data)):
        for i in range(len(data[j])):
            if data[j][i] == "@":
                rolls = 0
                neighbors = get_neighbors(j, i)
                for neighbor in neighbors:
                    if (
                        neighbor[0] < 0
                        or neighbor[0] >= len(data)
                        or neighbor[1] < 0
                        or neighbor[1] >= len(data[0])
                    ):
                        continue
                    if data[neighbor[0]][neighbor[1]] == "@":
                        rolls += 1
                if rolls < 4:
                    total += 1
    return total


def part_2(data: list[str]):
    total = 0
    while True:
        to_remove = []
        for j in range(len(data)):
            for i in range(len(data[j])):
                if data[j][i] == "@":
                    rolls = 0
                    neighbors = get_neighbors(j, i)
                    for neighbor in neighbors:
                        if (
                            neighbor[0] < 0
                            or neighbor[0] >= len(data)
                            or neighbor[1] < 0
                            or neighbor[1] >= len(data[0])
                        ):
                            continue
                        if data[neighbor[0]][neighbor[1]] == "@":
                            rolls += 1
                    if rolls < 4:
                        total += 1
                        to_remove.append((j, i))
        if not to_remove:
            break
        for j, i in to_remove:
            data[j] = data[j][:i] + "." + data[j][i + 1 :]

    return total


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))
