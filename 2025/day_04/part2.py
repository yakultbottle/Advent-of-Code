grid = [list(row) for row in open(0).read().strip().split("\n")]

width, height = len(grid[0]), len(grid)

dirs = ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))

def remove_paper():
    ans = 0
    for y in range(height):
        for x in range(width):
            if grid[y][x] == ".":
                continue

            adjacent = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if not (nx in range(width) and ny in range(height)):
                    continue
                if grid[ny][nx] == ".":
                    continue
                adjacent += 1

                if adjacent >= 4:
                    break
            else:
                grid[y][x] = "."
                ans += 1
    return ans

def print_grid():
    for y in range(height):
        print("".join(grid[y]))
    print()

ans = 0
removed = remove_paper()
while removed > 0:
    ans += removed
    removed = remove_paper()
print(ans)
