from collections import deque

input = open(0).read().strip()
grid = [list(line) for line in input.split()]

height, width = len(grid), len(grid[0])

start: tuple[int, int, int] = (-1, -1, -1)
end: tuple[int, int] = (-1, -1)
for y in range(height):
    for x in range(width):
        if grid[y][x] == "S":
            start = (x, y, 0)
            grid[y][x] = "a"
        if grid[y][x] == "E":
            end = (x, y)
            grid[y][x] = "z"

frontier: deque[tuple[int, int, int]] = deque([start])
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
seen = set([(start[0], start[1])])

while frontier:
    x, y, steps = frontier.pop()

    if (x, y) == end:
        print(steps)

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if not (nx in range(width) and ny in range(height)):
            continue
        if (nx, ny) in seen:
            continue
        if ord(grid[ny][nx]) - 1 > ord(grid[y][x]):
            continue

        seen.add((nx, ny))
        frontier.appendleft((nx, ny, steps + 1))
