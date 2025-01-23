import heapq

input = open(0).read().strip().split("\n")
grid = [[char for char in line] for line in input]

W, H = len(grid[0]), len(grid)

cost = [[1 for _ in range(W)] for _ in range(H)]
galaxies = []
for y in range(H):
    empty = True
    for x in range(W):
        if grid[y][x] == "#":
            empty = False
            galaxies.append((x, y))

    if empty:
        for x in range(W):
            cost[y][x] = 2

for x in range(W):
    empty = True
    for y in range(H):
        if grid[y][x] == "#":
            empty = False
            break

    if empty:
        for y in range(H):
            cost[y][x] = 2

seen = [[False for _ in range(W)] for _ in range(H)]
# dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
dirs = [(1, 0), (0, 1), (-1, 0)] # This change goes from 20s -> 8s
def bfs(og_x: int, og_y: int) -> int:
    frontier = []
    heapq.heappush(frontier, (0, og_x, og_y))
    vis = [[False for _ in range(W)] for _ in range(H)]
    sum = 0

    while frontier:
        dist, x, y = heapq.heappop(frontier)
        vis[y][x] = True

        if grid[y][x] == "#" and not seen[y][x]:
            sum += dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (nx in range(W) and ny in range(H)):
                continue
            if vis[ny][nx]:
                continue

            vis[ny][nx] = True
            heapq.heappush(frontier, (dist + cost[ny][nx], nx, ny))

    return sum

dists = 0
for x, y in galaxies:
    if not seen[y][x] and grid[y][x] == "#":
        temp = bfs(x, y)
        dists += temp
    seen[y][x] = True

print(dists)

