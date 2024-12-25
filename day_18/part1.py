import sys
from collections import deque

def read_data():
    input = [tuple([int(x) for x in pair.strip().split(",")]) for pair in sys.stdin.readlines()]
    return input

# print(read_data())

bytes = read_data()

if len(bytes) == 25:
    W = H = 6 + 1
    waiting_time = 12
else:
    W = H = 70 + 1
    waiting_time = 1024

grid = [[False for col in range(W)] for row in range(H)]

count = 0
for byte in bytes:
    if count == waiting_time:
        break
    x, y = byte
    grid[y][x] = True
    count += 1

# print(grid)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

frontier = deque([])
frontier.appendleft(((0, 0), 0))
grid[0][0] = True
output = -1
end = (W - 1, H - 1)

while frontier:
    curr, cost = frontier.pop()
    x, y = curr
    # grid[y][x] = True

    # print(f"{curr}, {cost}")
    if curr == end:
        output = cost
        break

    for dir in dirs:
        dx, dy = dir
        new_x, new_y = x + dx, y + dy

        if not (0 <= new_x < W and 0 <= new_y < H):
            continue
        if grid[new_y][new_x]:
            continue
        
        grid[new_y][new_x] = True
        frontier.appendleft(((new_x, new_y), cost + 1))

print(output)
