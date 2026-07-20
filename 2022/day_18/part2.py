input = open(0).read().strip().split("\n")

dirs = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))

MAX = 22
grid = [[[False for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]
sides = 0
for line in input:
    x, y, z = list(map(int, line.split(",")))
    grid[x + 1][y + 1][z + 1] = True

seen = [[[False for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]
seen_sides = set()
frontier = [(0, 0, 0)]

while frontier:
    x, y, z = frontier.pop()

    for dx, dy, dz in dirs:
        nx, ny, nz = x + dx, y + dy, z + dz

        if not (nx in range(MAX) and ny in range(MAX) and nz in range(MAX)):
            continue
        if seen[nx][ny][nz]:
            continue

        if grid[nx][ny][nz]:
            if (nx, ny, nz, dx, dy, dz) not in seen_sides:
                sides += 1
                seen_sides.add((nx, ny, nz, dx, dy, dz))
        else:
            seen[nx][ny][nz] = True
            frontier.append((nx, ny, nz))

print(sides)

