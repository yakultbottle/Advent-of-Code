import os
from collections import deque

input = open(0).read().strip().split("\n")

IS_TEST = "EXAMPLE" in os.environ
LOW, HIGH = (7, 27) if IS_TEST else (200000000000000, 400000000000000)

lines = deque()

for i, line in enumerate(input):
    position, velocity = [list(map(int, item.split(","))) for item in line.split("@")]

    px, py, _ = position
    vx, vy, _ = velocity

    gradient = vy / vx
    intersect = py - gradient * px

    lines.append((px, py, vx, vy, gradient, intersect))
n = len(lines)

count = 0
for i in range(n):
    for j in range(i + 1, n):
        px1, py1, vx1, vy1, m1, c1 = lines[i]
        px2, py2, vx2, vy2, m2, c2 = lines[j]

        if m1 == m2:
            continue

        x = (c2 - c1) / (m1 - m2)
        y = m1 * x + c1

        is_forward_in_time = (x - px1) / vx1 >= 0 and (x - px2) / vx2 >= 0

        if is_forward_in_time and LOW <= x <= HIGH and LOW <= y <= HIGH:
            count += 1

print(count)
