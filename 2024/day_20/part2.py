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

threshold = 100
def num_cheats(num_seconds: int, tile: tuple[int,int]) -> int:
    x, y = tile
    count = 0
    num_checks = num_seconds * 2
    dx = num_seconds
    dy = 0

    ddx = -1
    ddy = 1 # for now

    for _ in range(num_checks):
        nx, ny = x + dx, y + dy
        if (0 <= nx < W and 0 <= ny < H) and not walls[ny][nx]:
            start = time[y][x]
            end = time[ny][nx]
            if abs(end - start) - num_seconds >= threshold:
                # print((x, y), (nx, ny), sep=" : ")
                count += 1

        dx += ddx
        if dy == num_seconds:
            ddy = -1
        dy += ddy
    
    return count

count = 0
for tile in tiles:
    for num_seconds in range(2, 21):
        count += num_cheats(num_seconds, tile)
print(count)
