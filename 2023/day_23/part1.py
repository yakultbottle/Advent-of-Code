from collections import deque

grid = [list(row) for row in open(0).read().strip().split()]

width, height = len(grid[0]), len(grid)

start = (1, 0)
end = (width - 2, height - 1)
last = (-1, -1)

frontier: deque[tuple[int, ...]] = deque([start + last + (0,)])
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arrow_dirs = {
    ">": 0,
    "v": 1,
    "<": 2,
    "^": 3,
}

count = 0
while frontier:
    x, y, last_x, last_y, steps = frontier.popleft()

    if (x, y) == end:
        count = steps

    for direction, (dx, dy) in enumerate(dirs):
        nx, ny = x + dx, y + dy

        if not (nx in range(width) and ny in range(height)):
            continue
        if (nx, ny) == (last_x, last_y):
            continue
        if grid[ny][nx] == "#":
            continue
        if grid[ny][nx] in ">v<^" and arrow_dirs[grid[ny][nx]] != direction:
            continue

        frontier.append((nx, ny, x, y, steps + 1))

print(count)

