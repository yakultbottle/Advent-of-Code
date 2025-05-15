from copy import deepcopy

input = [list(row) for row in open(0).read().strip().split("\n")]

height, width = len(input), len(input[0])
dirs = [[0, -1], [-1, 0], [0, 1], [1, 0]]

NUM_ITERS = 1000000000

def step(grid: list[list[str]]):
    for dx, dy in dirs:
        i_range = range(height) if dy <= 0 else range(height - 1, -1, -1)
        j_range = range(width) if dx <= 0 else range(width - 1, -1, -1)

        for i in i_range:
            for j in j_range:
                if grid[i][j] != "O":
                    continue

                x, y = j, i
                while 0 - dx <= x < width - dx and 0 - dy <= y < height - dy and grid[y + dy][x + dx] == ".":
                    grid[y + dy][x + dx], grid[y][x] = grid[y][x], grid[y + dy][x + dx]
                    x += dx
                    y += dy

def hash_grid(grid: list[list[str]]) -> set:
    hash = set()
    for i in range(height):
        for j in range(width):
            if grid[i][j] != "O":
                continue
            hash.add((j, i))
    return hash

'''
# This is Floyd's algorithm of cycle detection
# https://www.geeksforgeeks.org/how-does-floyds-slow-and-fast-pointers-approach-work/
# Easier and more memory intensive is to hash and find when it repeats

fast, slow = deepcopy(input), deepcopy(input)

step(slow)
step(fast)
step(fast)

while hash_grid(fast) != hash_grid(slow):
    step(slow)
    step(fast)
    step(fast)

fast = input
head = 0
while hash_grid(fast) != hash_grid(slow):
    step(slow)
    step(fast)
    head += 1

step(fast)
cycle = 1
while hash_grid(fast) != hash_grid(slow):
    step(fast)
    cycle += 1

tail = (NUM_ITERS - head) % cycle
for _ in range(tail):
    step(fast)
grid = fast
'''

# This is the "trivial" solution, this takes 2.5s vs 9.6s of the above Floyd's solution
lookup = {}
grid = input
hash = hash_grid(grid)
lookup[tuple(hash)] = iter
head, cycle = 0, -1
for iter in range(NUM_ITERS):
    step(grid)
    hash = tuple(hash_grid(grid))
    if hash in lookup:
        head = lookup[hash]
        cycle = iter - head
        break
    lookup[hash] = iter

# there should be a cycle but whatever
tail = (NUM_ITERS - head) % cycle if cycle != -1 else 0
for _ in range(tail):
    step(grid)

load = 0
for i in range(height):
    for j in range(width):
        if grid[i][j] != "O":
            continue
        
        load += (height - i)
print(load)

