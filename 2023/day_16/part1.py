grid = [list(row) for row in open(0).read().strip().split("\n")]

height, width = len(grid), len(grid[0])
energised = [[[False for _ in range(4)] for _ in range(width)] for _ in range(height)]
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

frontier = []
frontier.append((0, 0, 0))

while frontier:
    x, y, dir = frontier.pop()
    dx, dy = dirs[dir]
    
    while 0 <= x < width and 0 <= y < height:
        if energised[y][x][dir]:
            break
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

for row in energised:
    print("".join(["#" if char[0] or char[1] or char[2] or char[3] else "." for char in row]))

count = sum([sum([1 if char[0] or char[1] or char[2] or char[3] else 0 for char in row]) for row in energised])
print(count)

