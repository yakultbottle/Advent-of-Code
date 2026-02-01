input = open(0).read().split()

blocks = []
max_x, max_y = 0, 0

for line in input:
    block = tuple(tuple(map(int, row.split(",")[::-1])) for row in line.split("~"))
    max_x = max(max_x, block[0][2], block[1][2])
    max_y = max(max_y, block[0][1], block[1][1])
    blocks.append(block)

height = [[[0, -1] for _ in range(max_x + 1)] for _ in range(max_y + 1)]
blocks.sort()
num_blocks = len(blocks)
cannot_remove = set()

for block_id, ((z1, y1, x1), (z2, y2, x2)) in enumerate(blocks):
    block_height = max(height[y][x][0] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)) + 1
    supports = set()

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            height_below, id_below = height[y][x]
            if height_below + 1 == block_height and id_below != -1:
                supports.add(id_below)
            height[y][x] = [block_height + (z2 - z1), block_id]

    if len(supports) == 1:
        cannot_remove |= supports

print(num_blocks - len(cannot_remove))
