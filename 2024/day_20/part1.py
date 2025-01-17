import sys
import copy
from collections import deque

maze = [list(line.strip()) for line in sys.stdin.readlines()]

H = len(maze)
W = len(maze[0])

walls = [[False for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if maze[i][j] == '#':
            walls[i][j] = True
        elif maze[i][j] == 'S':
            start = (j, i)
            maze[i][j] = '.'
        elif maze[i][j] == 'E':
            end = (j, i)
            maze[i][j] = '.'

dirs = [(1,0),(0,1),(-1,0),(0,-1)]
vis = copy.deepcopy(walls)
tiles = []
time = [[0 for _ in range(W)] for _ in range(H)]

curr_time = 0
frontier = deque([start])
while frontier:
    x, y = frontier.pop()
    time[y][x] = curr_time
    vis[y][x] = True
    tiles.append((x, y))
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if vis[ny][nx]:
            continue
        if not (0 <= x < W and 0 <= y < H):
            continue
        frontier.appendleft((nx, ny))
    curr_time += 1

# print(time[end[1]][end[0]])

def num_cheats(tile: tuple[int,int]) -> int:
    x, y = tile
    count = 0
    threshold = 100

    for dx, dy in [(2,0),(1,1),(0,2),(-1,1),(-2,0),(-1,-1),(0,-2),(1,-1)]:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < W and 0 <= ny < H):
            continue
        start = time[y][x]
        end = time[ny][nx]
        if end - start - 2 >= threshold:
            count += 1
    
    return count

count = 0
for tile in tiles:
    count += num_cheats(tile)
print(count)
