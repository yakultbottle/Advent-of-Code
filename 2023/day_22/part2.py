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
above = [list() for _ in range(num_blocks)]
below = [list() for _ in range(num_blocks)]

for block_id, ((z1, y1, x1), (z2, y2, x2)) in enumerate(blocks):
    block_height = max(height[y][x][0] for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)) + 1
    supports = set()

    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            height_below, id_below = height[y][x]
            if height_below + 1 == block_height and id_below != -1:
                supports.add(id_below)
            height[y][x] = [block_height + (z2 - z1), block_id]

    for support in supports:
        above[support].append(block_id)
        below[block_id].append(support)

def try_remove(block: int, fallen: set[int]) -> int:
    count = 0

    for potential in above[block]:
        for support in below[potential]:
            if support not in fallen:
                break
        else:
            fallen.add(potential)
            count += try_remove(potential, fallen) + 1

    return count

total = 0
for i in range(num_blocks):
    total += try_remove(i, set([i]))
print(total)

