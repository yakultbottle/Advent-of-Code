input = open(0).read().strip()

grid = [list(map(int, line)) for line in input.split("\n")]

n = len(grid)

dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))

ans = -1
for y in range(1, n - 1):
    for x in range(1, n - 1):
        scenic = 1

        for dx, dy in dirs:
            nx, ny = x, y

            for i in range(1, n):
                nx, ny = nx + dx, ny + dy

                if not (nx in range(n) and ny in range(n)):
                    scenic *= i - 1
                    break

                if grid[ny][nx] >= grid[y][x]:
                    scenic *= i
                    break

        ans = max(ans, scenic)

print(ans)
