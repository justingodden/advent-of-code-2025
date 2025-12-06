import os
from datetime import date

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

cookies = {"session": os.environ.get("AOC_COOKIE")}
today = date.today()


INIT_FUNC_CODE = """
from pathlib import Path

_dir = Path(__file__).parent

with open(_dir / "test_input.txt") as file:
    test_input = file.read().splitlines()

with open(_dir / "input.txt") as file:
    data = file.read().splitlines()


def part_1(data: list[str]):
    pass


def part_2(data: list[str]):
    pass


def solve():
    print(part_1(data))
    print(part_2(data))


def test():
    print(part_1(test_input))
    print(part_2(test_input))
"""


def get_aoc_input(day: int) -> str:
    url = f"https://adventofcode.com/{today.year}/day/{day}/input"

    r = requests.get(url, cookies=cookies)
    return r.text.rstrip()


def get_aoc_test_code(day: int) -> str:
    url = f"https://adventofcode.com/{today.year}/day/{day}"

    r = requests.get(url, cookies=cookies)
    soup = BeautifulSoup(r.content, "html.parser")

    codes = soup.find_all("code")
    max_len = 0
    test_code = ""

    for code in codes:
        if len(code.text) > max_len:
            max_len = len(code.text)
            test_code = code.text

    return test_code.rstrip()


def create_day_folder(day: int):
    solutions_folder = os.path.join(os.path.dirname(__file__), "solutions")
    folder_name = f"day_{day:02d}"
    folder_path = os.path.join(solutions_folder, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


def create_files(day: int, test_code: str, input_data: str):
    solutions_folder = os.path.join(os.path.dirname(__file__), "solutions")
    folder_name = f"day_{day:02d}"
    folder_path = os.path.join(solutions_folder, folder_name)

    test_file_path = os.path.join(folder_path, "test_input.txt")
    with open(test_file_path, "w") as f:
        f.write(test_code)

    input_file_path = os.path.join(folder_path, "input.txt")
    with open(input_file_path, "w") as f:
        f.write(input_data)

    solution_file_path = os.path.join(folder_path, "solution.py")
    with open(solution_file_path, "w") as f:
        f.write(INIT_FUNC_CODE.strip())

    init_file_path = os.path.join(folder_path, "__init__.py")
    with open(init_file_path, "w") as f:
        f.write(
            "from .solution import solve as solve\nfrom .solution import test as test"
        )


def add_module_to_init(day: int):
    solutions_folder = os.path.join(os.path.dirname(__file__), "solutions")
    init_file_path = os.path.join(solutions_folder, "__init__.py")
    with open(init_file_path, "a+") as f:
        f.seek(0)
        content = f.read()
        if f"day_{day:02d}" not in content:
            f.write(f"from . import day_{day:02d} as day_{day:02d}\n")


def init_aoc(day: int):
    create_day_folder(day)
    test_code = get_aoc_test_code(day)
    input_data = get_aoc_input(day)
    create_files(day, test_code, input_data)
    add_module_to_init(day)
