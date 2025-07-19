input = [line.split(" ") for line in open(0).read().strip().split("\n")]

dirs = {
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1),
    "R": (1, 0),
}
x, y = (0, 0)

coords = []
boundary = 0
for dir, length, colour in input:
    coords.append((x, y))
    dx, dy = [d * int(length) for d in dirs[dir]]
    x, y = x + dx, y + dy
    boundary += int(length)

# Using Gauss' shoelace method to find area of a polygon
area = 0
length = len(coords)
for i in range(length):
    area += coords[i][0] * coords[(i + 1) % length][1] - coords[((i + 1) % length)][0] * coords[i][1]
area = abs(area) // 2

# Using Pick's Theorem to convert Gauss' area into inner area
# A = I + B/2 - 1
inner_area = area - (boundary // 2) + 1

print(boundary + inner_area)
