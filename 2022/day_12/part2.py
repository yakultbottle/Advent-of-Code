from collections import deque

input = open(0).read().strip()
grid = [list(line) for line in input.split()]

height, width = len(grid), len(grid[0])

frontier: deque[tuple[int, int, int]] = deque()
dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
seen = set()

end: tuple[int, int] = (-1, -1)
for y in range(height):
    for x in range(width):
        if grid[y][x] == "S" or grid[y][x] == "a":
            frontier.append((x, y, 0))
            grid[y][x] = "a"
        if grid[y][x] == "E":
            end = (x, y)
            grid[y][x] = "z"

ans = float('inf')
while frontier:
    x, y, steps = frontier.pop()

    if (x, y) == end:
        ans = min(ans, steps)
        break

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

print(ans)
