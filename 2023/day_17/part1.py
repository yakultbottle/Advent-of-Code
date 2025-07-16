import heapq

grid = [list(row) for row in open(0).read().strip().split("\n")]
height, width = len(grid), len(grid[0])

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pq = []
heapq.heappush(pq, (0, 0, 0, 0, 0))
best = {}

answer = float('inf')
while pq:
    cost, x, y, num_consecutive, dir = heapq.heappop(pq)
    if (x, y, num_consecutive, dir) in best and cost >= best[(x, y, num_consecutive, dir)]:
        continue
    best[(x, y, num_consecutive, dir)] = cost
    # print(f"({x}, {y}) -> cost {cost}")
    if x == width - 1 and y == height - 1:
        answer = cost
        break

    left, right = (dir + 1) % 4, (dir + 3) % 4

    if num_consecutive < 3:
        dx, dy = dirs[dir]
        nx, ny = x + dx, y + dy
        if nx in range(width) and ny in range(height):
            heapq.heappush(pq, (cost + int(grid[ny][nx]), nx, ny, num_consecutive + 1, dir))
    dx, dy = dirs[left]
    nx, ny = x + dx, y + dy
    if nx in range(width) and ny in range(height):
        heapq.heappush(pq, (cost + int(grid[ny][nx]), nx, ny, 1, left))
    dx, dy = dirs[right]
    nx, ny = x + dx, y + dy
    if nx in range(width) and ny in range(height):
        heapq.heappush(pq, (cost + int(grid[ny][nx]), nx, ny, 1, right))

print(answer)

