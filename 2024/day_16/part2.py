import sys
from heapq import heappush, heappop
from collections import defaultdict

def read_data() -> list[list[str]]:
    return [list(line.strip()) for line in sys.stdin.readlines()]

path = set()
def main(maze: list[list[str]]) -> int:
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == "S":
                start = (j, i)
                maze[i][j] = "."
            if maze[i][j] == "E":
                end = (j, i)
                maze[i][j] = "."

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    pq = [(0, 0, start)]
    vis = defaultdict(lambda: float('inf'))
    parent = defaultdict(list)
    min_dist = float('inf')

    while pq:
        dist, dir, pos = heappop(pq)
        
        if dist > min_dist:
            continue
        
        if dist > vis[(dir, pos)]:
            continue
        vis[(dir, pos)] = dist

        if pos == end:
            if dist < min_dist:
                min_dist = dist
                end_dirs = {dir}
            elif dist == min_dist:
                end_dirs.add(dir)
            continue

        x, y = pos

        cw = (dir + 1) % 4
        if dist + 1000 < vis[(cw, pos)]:
            vis[(cw, pos)] = dist + 1000
            parent[(cw, pos)] = [(dir, pos)]
            heappush(pq, ((dist + 1000), cw, pos))
        elif dist + 1000 == vis[(cw, pos)]:
            if (dir, pos) not in parent[(cw, pos)]:
                parent[(cw, pos)].append((dir, pos))
                heappush(pq, ((dist + 1000), cw, pos))
        ccw = (dir - 1) % 4
        if dist + 1000 < vis[(ccw, pos)]:
            vis[(ccw, pos)] = dist + 1000
            parent[(ccw, pos)] = [(dir, pos)]
            heappush(pq, ((dist + 1000), ccw, pos))
        elif dist + 1000 == vis[(ccw, pos)]:
            if (dir, pos) not in parent[(ccw, pos)]:
                parent[(ccw, pos)].append((dir, pos))
                heappush(pq, ((dist + 1000), ccw, pos))

        dx, dy = dirs[dir]
        new_x = x + dx
        new_y = y + dy
        if maze[new_y][new_x] == "#":
            continue
        new_pos = (new_x, new_y)
        if dist + 1 < vis[(dir, new_pos)]:
            vis[(dir, new_pos)] = dist + 1
            parent[(dir, new_pos)] = [(dir, pos)]
            heappush(pq, ((dist + 1), dir, new_pos))
        elif dist + 1 == vis[(dir, new_pos)]:
            parent[(dir, new_pos)].append((dir, pos))
            heappush(pq, ((dist + 1), dir, new_pos))

    stack = []
    vis = set()
    path.add(end)
    for end_dir in end_dirs:
        stack.append((end_dir, end))

    while stack:
        dir, pos = stack.pop()
        parents = parent[(dir, pos)]
        if (dir, pos) in vis:
            continue
        vis.add((dir, pos))
        path.add(pos)
        for p in parents:
            stack.append(p)

    for tile in path:
        x, y = tile
        maze[y][x] = "O"
    return len(path)

def print_maze(maze: list[list[str]]):
    for i in range(len(maze)):
        print("".join(maze[i]))

if __name__ == "__main__":
    maze = read_data()
    output = main(maze)
    # print_maze(maze)
    print(output)
