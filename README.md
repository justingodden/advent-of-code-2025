# Advent of Code 2025 🎄

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) in Python.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

1. Clone the repository
2. Create a `.env` file in the root directory with your AoC session cookie:
   ```
   AOC_COOKIE=your_session_cookie_here
   ```
   (You can find this in your browser's cookies after logging into adventofcode.com)

3. Install dependencies:
   ```bash
   uv sync
   ```

## Commands

### Initialize a Day

```bash
uv run init.py [day]
```

Creates a new day folder with:
- `input.txt` - Your puzzle input (fetched from AoC)
- `test_input.txt` - Example input from the puzzle description
- `solution.py` - Template with `part_1()`, `part_2()`, `test()`, and `solve()` functions

If no day is specified, it defaults to today's date.

**Example:**
```bash
uv run init.py 5    # Initialize day 5
uv run init.py      # Initialize today's puzzle
```

### Test Your Solution

```bash
uv run test.py [day]
```

Runs your solution against the test input (`test_input.txt`).

**Example:**
```bash
uv run test.py 5    # Test day 5's solution
uv run test.py      # Test today's solution
```

### Solve the Puzzle

```bash
uv run solve.py [day]
```

Runs your solution against the actual input (`input.txt`).

**Example:**
```bash
uv run solve.py 5   # Solve day 5
uv run solve.py     # Solve today's puzzle
```

## Project Structure

```
aoc-2025/
├── init.py              # Initialize a new day
├── test.py              # Run against test input
├── solve.py             # Run against actual input
├── pyproject.toml
└── src/aoc_2025/
    ├── utils.py         # Helper functions for fetching inputs
    └── solutions/
        ├── day_01/
        │   ├── input.txt
        │   ├── test_input.txt
        │   └── solution.py
        ├── day_02/
        │   └── ...
        └── ...
```

## Requirements

- Python >= 3.11
- uv
