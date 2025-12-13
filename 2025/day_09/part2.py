coords = [tuple(map(int, row.split(","))) for row in open(0).read().strip().split("\n")]
n = len(coords)

xs = {x for x, _ in coords}
ys = {y for _, y in coords}

cmap_x = {x: i for i, x in enumerate(sorted(xs))}
cmap_y = {y: i for i, y in enumerate(sorted(ys))}

width, height = len(xs), len(ys)
boundary = set()

for i in range(n):
    x1, x2 = cmap_x[coords[i][0]], cmap_x[coords[i - 1][0]]
    y1, y2 = cmap_y[coords[i][1]], cmap_y[coords[i - 1][1]]

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            boundary.add((x, y))

grid = [[1] * width for _ in range(height)]
frontier = []
seen = set()
frontier.append((-1, -1))
seen.add((-1, -1))
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
while frontier:
    x, y = frontier.pop()

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if nx < -1 or nx > width or ny < -1 or ny > height:
            continue
        if (nx, ny) in boundary:
            continue
        if (nx, ny) in seen:
            continue
        seen.add((nx, ny))
        if 0 <= nx < width and 0 <= ny < height:
            grid[ny][nx] = 0
        frontier.append((nx, ny))

def rect_area(one: tuple[int, int], two: tuple[int, int]) -> int:
    first = abs(one[0] - two[0]) + 1
    second = abs(one[1] - two[1]) + 1
    return first * second

class PrefixSum2D:
    def __init__(self, grid: list[list[int]]):
        self.grid = [[0] * width for _ in range(height)]
        for y in range(height):
            for x in range(width):
                top = self.grid[y - 1][x] if y > 0 else 0
                left = self.grid[y][x - 1] if x > 0 else 0
                topleft = self.grid[y - 1][x - 1] if y > 0 and x > 0 else 0
                self.grid[y][x] = grid[y][x] + top + left - topleft

    def is_valid(self, one: tuple[int, int], two: tuple[int, int]) -> bool:
        x1, y1 = min(one[0], two[0]), min(one[1], two[1])
        x2, y2 = max(one[0], two[0]), max(one[1], two[1])
        x1 = cmap_x[x1]
        x2 = cmap_x[x2]
        y1 = cmap_y[y1]
        y2 = cmap_y[y2]

        top = self.grid[y1 - 1][x2] if y1 > 0 else 0
        left = self.grid[y2][x1 - 1] if x1 > 0 else 0
        topleft = self.grid[y1 - 1][x1 - 1] if x1 > 0 and y1 > 0 else 0
        count = self.grid[y2][x2] - top - left + topleft
        return count == rect_area((x1, y1), (x2, y2))

    def __str__(self):
        temp = []
        for row in self.grid:
            temp.append(" ".join(list(map(str, row))))
        return "\n".join(temp)

psa = PrefixSum2D(grid)
# print(psa)

def is_valid(one: tuple[int, int], two: tuple[int, int]) -> bool:
    x1, y1 = cmap_x[one[0]], cmap_y[one[1]]
    x2, y2 = cmap_x[two[0]], cmap_y[two[1]]

    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if not grid[y][x]:
                return False
    return True

maxArea = -1
for i in range(n):
    for j in range(i + 1, n):
        area = rect_area(coords[i], coords[j])
        if area > maxArea and psa.is_valid(coords[i], coords[j]):
            maxArea = area
print(maxArea)
