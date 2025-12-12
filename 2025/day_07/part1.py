grid = [list(row) for row in open(0).read().strip().split("\n")]

height, width = len(grid), len(grid[0])

start = (-1, -1)
for y in range(height):
    for x in range(width):
        if grid[y][x] == "S":
            start = (x, y)
            break

frontier = [start]
seen = set(start)
splitters = set()

while frontier:
    x, y = frontier.pop()

    if grid[y][x] == "^":
        splitters.add((x, y))
        for dx, dy in ((x - 1, y), (x + 1, y)):
            if not (dx in range(width) and dy in range(height)):
                continue
            if (dx, dy) in seen:
                continue
            seen.add((dx, dy))
            frontier.append((dx, dy))
    else:
        dx, dy = x, y + 1
        if not (dx in range(width) and dy in range(height)):
            continue
        if (dx, dy) in seen:
            continue
        seen.add((dx, dy))
        frontier.append((dx, dy))

print(len(splitters))

