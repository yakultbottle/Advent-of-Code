import sys
from copy import deepcopy

sys.setrecursionlimit(100000)

grid = open(0).read().strip().split("\n")
W, H = len(grid[0]), len(grid)

global_seen = [[False for _ in range(W)] for _ in range(H)]
start = (-1, -1)
for y in range(H):
    for x in range(W):
        if grid[y][x] == "S":
            start = (x, y)
            global_seen[y][x] = True
            break

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pipes = [("-", "J", "7"), ("|", "J", "L"), ("-", "L", "F"), ("|", "7", "F")]

def dfs(prev_dir: int, x: int, y: int, dist: int) -> int:
    if (x, y) == start:
        return dist

    curr_pipe = grid[y][x]

    if curr_pipe not in pipes[prev_dir]:
        return -1

    next_dir = 0
    for dir in range(4):
        if dir == (prev_dir + 2 % 4):
            continue

        dx, dy = dirs[dir]
        nx, ny = x + dx, y + dy

        if not (nx in range(W) and ny in range(H)):
            continue
        if seen[ny][nx] and not (nx, ny) == start:
            continue
        
        if curr_pipe in pipes[(dir + 2) % 4]:
            next_dir = dir
            break

    dx, dy = dirs[next_dir]
    nx, ny = x + dx, y + dy
    seen[ny][nx] = True
    return dfs(next_dir, nx, ny, dist + 1)

max_loop = 0
for dir in range(4):
    x, y = start
    dx, dy = dirs[dir]
    nx, ny = x + dx, y + dy

    if not (nx in range(W) and ny in range(H)):
        continue
    if global_seen[ny][nx]:
        continue

    seen = deepcopy(global_seen)
    seen[ny][nx] = True
    size_of_loop = dfs(dir, nx, ny, 1)
    max_loop = max(max_loop, size_of_loop)

print(max_loop // 2)
