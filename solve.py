import sys
from datetime import date

from aoc_2025 import solutions

today = date.today()
if len(sys.argv) == 1:
    day = today.day
elif len(sys.argv) == 2:
    day = int(sys.argv[1])
else:
    raise Exception("Need date argument. Or none for today's date.")


module = getattr(solutions, f"day_{day:02d}")
module.solve()
