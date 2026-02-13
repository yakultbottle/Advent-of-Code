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

adj_list = {junc: {} for junc in junctions}

for junc in junctions:
    sx, sy = junc
    stack = [(sx, sy, 0)]
    seen = {(sx, sy)}

    while stack:
        x, y, steps = stack.pop()
        seen.add((x, y))

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (nx in range(width) and ny in range(height)):
                continue
            if grid[ny][nx] == "#":
                continue
            if (nx, ny) in seen:
                continue

            if (nx, ny) != junc and (nx, ny) in junctions:
                adj_list[junc][(nx, ny)] = steps + 1
            else:
                stack.append((nx, ny, steps + 1))

fast_adj_list = {}
int_map = {}

for i, node in enumerate(junctions):
    int_map[node] = 2**i
for here, there in adj_list.items():
    fast_adj_list[int_map[here]] = {int_map[node]: weight for node, weight in there.items()}

def dfs(curr: int, visited: int) -> int:
    if curr == int_map[end]:
        return 0

    maximum = -float('inf')
    for next in fast_adj_list[curr]:
        if visited & next:
            continue
        maximum = max(maximum, dfs(next, visited | curr) + fast_adj_list[curr][next])

    return maximum

ans = dfs(int_map[start], 0)
print(ans)

