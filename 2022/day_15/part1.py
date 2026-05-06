import re
import os

input = open(0).read().strip().split("\n")

IS_TEST = "EXAMPLE" in os.environ
row = 10 if IS_TEST else 2000000

seen = set()
beacon_on_row = set()
for line in input:
    sx, sy, bx, by = list(map(int, re.findall(r"-?\d+", line)))

    if by == row:
        beacon_on_row.add(bx)

    manhattan_dist = abs(sx - bx) + abs(sy - by)
    dist_to_row = abs(row - sy)

    if dist_to_row > manhattan_dist:
        continue

    offset = manhattan_dist - dist_to_row

    for x in range(sx - offset, sx + offset + 1):
        seen.add(x)

ans = len(seen) - len(beacon_on_row)
print(ans)
