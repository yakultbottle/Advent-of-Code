import heapq

grid = [list(row) for row in open(0).read().strip().split("\n")]
height, width = len(grid), len(grid[0])

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pq = []
heapq.heappush(pq, (0, 0, 0, 0, 0))
best = {}

def try_move(x: int, y: int, num_consecutive: int, dir: int) -> None:
    dx, dy = dirs[dir]
    nx, ny = x + dx, y + dy
    if not (nx in range(width) and ny in range(height)):
        return
    heapq.heappush(pq, (cost + int(grid[ny][nx]), nx, ny, num_consecutive, dir))

answer = float('inf')
max_consecutive = 10
min_to_turn = 4
while pq:
    cost, x, y, num_consecutive, straight = heapq.heappop(pq)
    if x == width - 1 and y == height - 1:
        answer = cost
        break

    if (x, y, num_consecutive, straight) in best and cost >= best[(x, y, num_consecutive, straight)]:
        continue
    best[(x, y, num_consecutive, straight)] = cost

    if num_consecutive < max_consecutive:
        try_move(x, y, num_consecutive + 1, straight)
    if num_consecutive >= min_to_turn:
        left, right = (straight + 1) % 4, (straight + 3) % 4
        try_move(x, y, 1, left)
        try_move(x, y, 1, right)

print(answer)

