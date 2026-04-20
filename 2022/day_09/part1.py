input = open(0).read().strip().splitlines()

dirs = {
    "L": (-1, 0),
    "D": (0, 1),
    "U": (0, -1),
    "R": (1, 0),
}

head = [0, 5]
tail = [0, 5]

seen = set()
seen.add(tuple(tail))

for line in input:
    dir, steps = line.split()
    dx, dy = dirs[dir]

    for _ in range(int(steps)):
        head[0] += dx
        head[1] += dy

        diff_x = head[0] - tail[0]
        diff_y = head[1] - tail[1]

        if abs(diff_x) + abs(diff_y) > 2:
            tail[0] += 1 if head[0] > tail[0] else -1
            tail[1] += 1 if head[1] > tail[1] else -1
        elif diff_x > 1 or diff_x < -1:
            tail[0] += 1 if diff_x > 0 else -1
        elif diff_y > 1 or diff_y < -1:
            tail[1] += 1 if diff_y > 0 else -1

        seen.add(tuple(tail))

print(len(seen))

