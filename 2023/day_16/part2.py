from typing import Iterator

grid = [list(row) for row in open(0).read().strip().split("\n")]

height, width = len(grid), len(grid[0])
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def grid_walls(width: int, height: int) -> Iterator[tuple[int, int, int]]:
    for y in range(height):
        yield (0, y, 0)
    for x in range(width):
        yield (x, 0, 1)
    for y in range(height):
        yield (width - 1, y, 2)
    for x in range(width):
        yield (x, height - 1, 3)

count = 0
for start_x, start_y, start_dir in grid_walls(width, height):
    curr_count = 0
    energised = [[[False for _ in range(4)] for _ in range(width)] for _ in range(height)]
    frontier = []
    frontier.append((start_x, start_y, start_dir))

    while frontier:
        x, y, dir = frontier.pop()
        dx, dy = dirs[dir]
        
        while 0 <= x < width and 0 <= y < height:
            if energised[y][x][dir]:
                break
            curr_count += (1 if not any(energised[y][x]) else 0)
            energised[y][x][dir] = True
            if grid[y][x] == "/":
                dir = 3 - dir
            elif grid[y][x] == "\\":
                dir ^= 1
            elif grid[y][x] == "-" and dy:
                frontier.append((x, y, 0))
                frontier.append((x, y, 2))
                break
            elif grid[y][x] == "|" and dx:
                frontier.append((x, y, 1))
                frontier.append((x, y, 3))
                break
            dx, dy = dirs[dir]
            x, y = x + dx, y + dy

    count = max(count, curr_count)
    # print(start_x, start_y)

print(count)

