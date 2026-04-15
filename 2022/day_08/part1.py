input = open(0).read().strip()

grid = [list(map(int, line)) for line in input.split("\n")]

n = len(grid)

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
seen = set()

frontier = []

for num in range(n):
    seen.add((0, num))
    seen.add((n - 1, num))
    seen.add((num, 0))
    seen.add((num, n - 1))

    if num == 0 or num == n - 1:
        continue

    frontier.append((0, num, 0))
    frontier.append((num, 0, 1))
    frontier.append((n - 1, num, 2))
    frontier.append((num, n - 1, 3))

while frontier:
    x, y, dir = frontier.pop()
    dx, dy = dirs[dir]
    tallest_obstacle = grid[y][x]

    while True:
        nx, ny = x + dx, y + dy

        if not (nx in range(n) and ny in range(n)):
            break

        if grid[ny][nx] > tallest_obstacle:
            tallest_obstacle = grid[ny][nx]
            seen.add((nx, ny))

        x, y = nx, ny

print(len(seen))

