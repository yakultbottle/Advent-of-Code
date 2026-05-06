import re
import os

input = open(0).read().strip().split("\n")

IS_TEST = "EXAMPLE" in os.environ
bound = 20 if IS_TEST else 4000000
tuning_frequency = 4000000

upslopes = []
downslopes = []

for line in input:
    sx, sy, bx, by = list(map(int, re.findall(r"-?\d+", line)))
    manhattan_dist = abs(sx - bx) + abs(sy - by)

    # Store y-intercept
    left_top = sy + manhattan_dist - sx
    top_right = sy + manhattan_dist + sx
    left_bot = sy - manhattan_dist + sx
    bot_right = sy - manhattan_dist - sx

    upslopes.append((left_top, range(sx - manhattan_dist, sx)))
    upslopes.append((bot_right, range(sx, sx + manhattan_dist)))
    downslopes.append((top_right, range(sy, sy + manhattan_dist)))
    downslopes.append((left_bot, range(sy - manhattan_dist, sy)))

candidates = set()
for upslope, x_range in upslopes:
    for downslope, y_range in downslopes:
        x = (downslope - upslope) // 2
        y = x + upslope

        if not (x in x_range and y in y_range):
            continue

        for nx, ny in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1), (x + 1, y + 1), (x + 1, y - 1), (x - 1, y + 1), (x - 1, y - 1)):
            if not (nx in range(bound +  1) and ny in range(bound + 1)):
                continue

            candidates.add((nx, ny))

for line in input:
    sx, sy, bx, by = list(map(int, re.findall(r"-?\d+", line)))
    manhattan_dist = abs(sx - bx) + abs(sy - by)

    for cx, cy in list(candidates):
        dist = abs(sx - cx) + abs(sy - cy)

        if dist <= manhattan_dist:
            candidates.remove((cx, cy))

assert len(candidates) == 1
x, y = list(candidates).pop()
ans = x * tuning_frequency + y
print(ans)
