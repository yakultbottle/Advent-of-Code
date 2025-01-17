import sys

grid = sys.stdin.read().strip().split("\n") # list[str]
W, H = len(grid[0]), len(grid)

numbers = set(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
dirs = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
seen = set()

answer = 0
for y in range(H):
    for x in range(W):
        if grid[y][x] in numbers:
            continue
        if grid[y][x] != "*":
            continue

        gears = []
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if (nx, ny) in seen:
                continue
            if not (nx in range(W) and ny in range(H)):
                continue
            if grid[ny][nx] == ".":
                continue

            nx -= 1
            while nx in range(W):
                if grid[ny][nx] not in numbers:
                    break
                nx -= 1
            nx += 1

            number = 0
            while nx in range(W) and grid[ny][nx] in numbers:
                seen.add((nx, ny))
                number = number * 10 + int(grid[ny][nx])
                nx += 1
            gears.append(number)

        if len(gears) != 2:
            continue
        answer += gears[0] * gears[1]

print(answer)
