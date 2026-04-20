input = open(0).read().strip().splitlines()

dirs = {
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1),
    "R": (1, 0),
}

string = [[0, 5] for _ in range(10)]
head = string[0]
tail = string[-1]

# GRID_SIZE = 6
# grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# def print_grid():
#     for line in grid:
#         print("".join(line))
#     print()

seen = set()
seen.add(tuple(tail))

def update_tail(n: int):
    head = string[n]
    tail = string[n + 1]

    diff_x = head[0] - tail[0]
    diff_y = head[1] - tail[1]

    if abs(diff_x) + abs(diff_y) > 2:
        tail[0] += 1 if head[0] > tail[0] else -1
        tail[1] += 1 if head[1] > tail[1] else -1
    elif diff_x > 1 or diff_x < -1:
        tail[0] += 1 if diff_x > 0 else -1
    elif diff_y > 1 or diff_y < -1:
        tail[1] += 1 if diff_y > 0 else -1


for line in input:
    dir, steps = line.split()
    dx, dy = dirs[dir]

    # print(f"=== {dir}: {steps} ===")

    for _ in range(int(steps)):
        # grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

        head[0] += dx
        head[1] += dy

        for i in range(9):
            update_tail(i)

        # grid[head[1]][head[0]] = "H"
        # for i in range(9):
        #     rep = str(i) if i > 0 else "H"
        #     grid[string[i][1]][string[i][0]] = rep
        # print_grid()

        seen.add(tuple(tail))

print(len(seen))

