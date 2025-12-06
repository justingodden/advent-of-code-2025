import os
import sys
from datetime import date

from aoc_2025.utils import init_aoc

today = date.today()
if len(sys.argv) == 1:
    day = today.day
elif len(sys.argv) == 2:
    day = int(sys.argv[1])
else:
    raise Exception("Need date argument. Or none for today's date.")

if not os.path.exists(f"src/aoc_2025/solutions/day_{day:02d}"):
    init_aoc(day)
