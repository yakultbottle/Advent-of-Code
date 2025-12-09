grid = [list(row) for row in open(0).read().strip().split("\n")]

height, width = len(grid), len(grid[0])

start = (-1, -1)
for y in range(height):
    for x in range(width):
        if grid[y][x] == "S":
            start = (x, y)
            break

memo = {}
def travel_down(start: tuple[int, int]) -> int:
    if start in memo:
        return memo[start]

    x, y = start
    count = 0
    
    while (x in range(width) and y in range(height)) and grid[y][x] != "^":
        y += 1

    for dx, dy in ((x - 1, y), (x + 1, y)):
        if not (dx in range(width) and dy in range(height)):
            continue
        count += travel_down((dx, dy))

    memo[start] = count if count else 1
    return memo[start]

print(travel_down(start))

