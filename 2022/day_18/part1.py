input = open(0).read().strip().split("\n")

dirs = ((1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1))

MAX = 20
grid = [[[False for _ in range(MAX)] for _ in range(MAX)] for _ in range(MAX)]
sides = 0
for line in input:
    x, y, z = list(map(int, line.split(",")))
    grid[x][y][z] = True
    sides += 6

    for dx, dy, dz in dirs:
        nx, ny, nz = x + dx, y + dy, z + dz

        if not (nx in range(MAX) and ny in range(MAX) and nz in range(MAX)):
            continue

        if grid[nx][ny][nz]:
            sides -= 2

print(sides)
