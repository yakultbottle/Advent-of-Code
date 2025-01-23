input = open(0).read().strip().split("\n")
grid = [[char for char in line] for line in input]

W, H = len(grid[0]), len(grid)

is_empty_x = []
is_empty_y = []
galaxies = []
for y in range(H):
    empty = True
    for x in range(W):
        if grid[y][x] == "#":
            empty = False
            galaxies.append((x, y))

    if empty:
        is_empty_y.append(y)

for x in range(W):
    empty = True
    for y in range(H):
        if grid[y][x] == "#":
            empty = False
            break

    if empty:
        is_empty_x.append(x)

empty_gap = 2 - 1
dists = 0
for i in range(len(galaxies)):
    x1, y1 = galaxies[i]
    for j in range(i + 1, len(galaxies)):
        x2, y2 = galaxies[j]

        diff = abs(x1 - x2) + abs(y1 - y2)

        for empty_x in is_empty_x:
            if min(x1, x2) < empty_x < max(x1, x2):
                diff += empty_gap
        for empty_y in is_empty_y:
            if min(y1, y2) < empty_y < max(y1, y2):
                diff += empty_gap

        dists += diff

print(dists)

