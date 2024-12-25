import sys
from collections import deque

def read_data():
    input = [tuple([int(x) for x in pair.strip().split(",")]) for pair in sys.stdin.readlines()]
    return input

# print(read_data())

bytes = read_data()

if len(bytes) == 25:
    W = H = 6 + 1
    waiting_time = 12
else:
    W = H = 70 + 1
    waiting_time = 1024

def find_path(waiting_time: int):
    grid = [[False for col in range(W)] for row in range(H)]

    count = 0
    for byte in bytes:
        if count == waiting_time:
            break
        x, y = byte
        grid[y][x] = True
        count += 1

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    frontier = deque([])
    frontier.appendleft(((0, 0), 0))
    grid[0][0] = True
    output = -1
    end = (W - 1, H - 1)

    while frontier:
        curr, cost = frontier.pop()
        x, y = curr

        if curr == end:
            return True

        for dir in dirs:
            dx, dy = dir
            new_x, new_y = x + dx, y + dy

            if not (0 <= new_x < W and 0 <= new_y < H):
                continue
            if grid[new_y][new_x]:
                continue
            
            grid[new_y][new_x] = True
            frontier.appendleft(((new_x, new_y), cost + 1))

    return False

start = waiting_time + 1
end = len(bytes) - 1
min_fail_time = float('inf')
while start <= end:
    mid = (start + end) // 2

    res = find_path(mid)
    print(f"{mid}: {res}")

    if res:
        start = mid + 1
    else:
        min_fail_time = min(min_fail_time, mid)
        end = mid - 1

index = min_fail_time - 1 # 0-indexed issues
answer = bytes[index]
print()
print(f"second {min_fail_time}: {answer}")
