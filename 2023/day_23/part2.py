from collections import deque, defaultdict

grid = [list(row) for row in open(0).read().strip().split()]

width, height = len(grid[0]), len(grid)

start = (1, 0)
end = (width - 2, height - 1)

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
arrow_dirs = {
    ">": 0,
    "v": 1,
    "<": 2,
    "^": 3,
}

junctions = set()
junctions.add(start)
junctions.add(end)

for y in range(height):
    for x in range(width):
        if grid[y][x] == "#":
            continue

        count = 0
        for nx, ny in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
            if not (nx in range(width) and ny in range(height)):
                continue
            if grid[ny][nx] != "#":
                count += 1
        if count > 2:
            junctions.add((x, y))

seen = [[False for _ in range(width)] for _ in range(height)]

def find_next_junction(x: int, y: int, steps: int) -> tuple[int, int, int]:
    if (x, y) in junctions:
        return (x, y, steps)
    seen[y][x] = True

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if not (nx in range(width) and ny in range(height)):
            continue
        if grid[ny][nx] == "#":
            continue
        if seen[ny][nx]:
            continue

        return find_next_junction(nx, ny, steps + 1)

frontier: deque[tuple[int, int]] = deque([start])
adj_list = defaultdict(list)

while frontier:
    x, y = frontier.popleft()
    seen[y][x] = True

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy

        if not (nx in range(width) and ny in range(height)):
            continue
        if grid[ny][nx] == "#":
            continue
        if seen[ny][nx]:
            continue

        new_x, new_y, steps = find_next_junction(nx, ny, 1)
        adj_list[(new_x, new_y)].append((x, y, steps))
        adj_list[(x, y)].append((new_x, new_y, steps))
        frontier.append((new_x, new_y))

visited = set()
def dfs(x: int, y: int, steps: int) -> int:
    if (x, y) == end:
        return steps

    visited.add((x, y))

    maximum = -1
    for nx, ny, num_steps in adj_list[(x, y)]:
        if (nx, ny) in visited:
            continue
        candidate = dfs(nx, ny, steps + num_steps)
        maximum = max(maximum, candidate)

    visited.remove((x, y))
    return maximum

ans = dfs(start[0], start[1], 0)
print(ans)
