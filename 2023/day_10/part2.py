import sys
from copy import deepcopy

sys.setrecursionlimit(100000)

grid = open(0).read().strip().split("\n")
grid = [[char for char in line] for line in grid]

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
    global end
    if (x, y) == start:
        dx, dy = dirs[(prev_dir + 2) % 4]
        nx, ny = x + dx, y + dy
        end = (nx, ny)
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

best_seen = []
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

    if size_of_loop > max_loop:
        max_loop = size_of_loop
        best_seen = seen
        starting = (nx, ny)
        ending = end

x, y = start
x1, y1 = starting
x2, y2 = ending

if abs(x1 - x2) == 2:
    grid[y][x] = "-"
elif abs(y1 - y2) == 2:
    grid[y][x] = "|"
elif x == x1 + 1 or x == x2 + 1:
    if y1 > y or y2 > y:
        grid[y][x] = "7"
    else:
        grid[y][x] = "J"
else:
    if y1 > y or y2 > y:
        grid[y][x] = "F"
    else:
        grid[y][x] = "L"

inside = 0
for y in range(H):
    for x in range(W):
        if best_seen[y][x]:
            continue

        nx, ny = x, y
        intersections = 0
        wall = False
        J_wall, L_wall = False, False
        while ny >= 0:
            if best_seen[ny][nx]:
                if grid[ny][nx] == "J":
                    J_wall = True
                    wall = True
                elif grid[ny][nx] == "L":
                    L_wall = True
                    wall = True

                elif J_wall:
                    if grid[ny][nx] == "7":
                        J_wall = False
                        wall = False
                    elif grid[ny][nx] == "F":
                        J_wall = False
                        wall = False
                        intersections += 1
                elif L_wall:
                    if grid[ny][nx] == "F":
                        L_wall = False
                        wall = False
                    elif grid[ny][nx] == "7":
                        L_wall = False
                        wall = False
                        intersections += 1
                else:
                    intersections += 1

            ny -= 1

        if intersections & 1:
            inside += 1
        
print(inside)
