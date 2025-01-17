import sys
from heapq import heappush, heappop
from collections import defaultdict

def read_data() -> list[list[str]]:
    return [list(line.strip()) for line in sys.stdin.readlines()]

def main(maze: list[list[str]]) -> int:
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                here = (j, i)
                maze[i][j] = "."
            if maze[i][j] == "E":
                end = (j, i)
                maze[i][j] = "."

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pq = [(0, 0, here)]
    vis = defaultdict(lambda: float('inf'))

    while pq:
        dist, dir, pos = heappop(pq)
        
        if pos == end:
            return dist
        
        vis[(dir, pos)] = dist

        x, y = pos

        cw = (dir + 1) % 4
        if dist + 1000 < vis[(cw, pos)]:
            heappush(pq, ((dist + 1000), cw, pos))
        ccw = (dir - 1) % 4
        if dist + 1000 < vis[(ccw, pos)]:
            heappush(pq, ((dist + 1000), ccw, pos))

        dx, dy = dirs[dir]
        new_x = x + dx
        new_y = y + dy
        if maze[new_y][new_x] == "#":
            continue
        new_pos = (new_x, new_y)
        if dist + 1 < vis[(dir, new_pos)]:
            heappush(pq, ((dist + 1), dir, new_pos))
    return -1

def print_maze(maze: list[list[str]]):
    for i in range(len(maze)):
        print("".join(maze[i]))

if __name__ == "__main__":
    maze = read_data()
    # print_maze(maze)
    output = main(maze)
    print(output)
