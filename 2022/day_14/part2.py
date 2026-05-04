input = open(0).read().strip().split("\n")

min_x = min_y = float('inf')
max_x = max_y = -float('inf')

temp = []
for line in input:
    edges = [list(map(int, points.split(","))) for points in line.split(" -> ")]
    temp.append(edges)

    for x, y in edges:
        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)

offset_x = int(min_x) - 500
grid = [["." for _ in range(offset_x, int(max_x) + 500)] for _ in range(int(max_y) + 2)]

for edges in temp:
    old_x, old_y = edges.pop()
    for x, y in reversed(edges):
        if old_x - x > 0:
            for nx in range(x, old_x + 1):
                grid[y][nx - offset_x] = "#"
        elif old_x - x < 0:
            for nx in range(old_x, x + 1):
                grid[y][nx - offset_x] = "#"
        elif old_y - y > 0:
            for ny in range(y, old_y + 1):
                grid[ny][x - offset_x] = "#"
        elif old_y - y < 0:
            for ny in range(old_y, y + 1):
                grid[ny][x - offset_x] = "#"
        else:
            assert False
        old_x, old_y = x, y

def spawn_rock(x: int, y: int) -> bool:
    while True:
        if y >= max_y + 1:
            grid[int(max_y) + 1][x - offset_x] = "o"
            return False

        if grid[y + 1][x - offset_x] == ".":
            y += 1
        elif grid[y + 1][x - offset_x - 1] == ".":
            y += 1
            x -= 1
        elif grid[y + 1][x - offset_x + 1] == ".":
            y += 1
            x += 1
        else:
            grid[y][x - offset_x] = "o"
            return True

count = 0
while grid[0][500 - offset_x] != "o":
    spawn_rock(500, 0)
    count += 1
print(count)
