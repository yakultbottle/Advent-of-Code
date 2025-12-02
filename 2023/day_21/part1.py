grid: list[list[str]] = [list(string) for string in open(0).read().strip().split("\n")]

width, height = len(grid[0]), len(grid)
assert(width == height)

odd_count, even_count = 0, 1
odd_frontier, even_frontier = [(width // 2, height // 2)], []


def process_step(frontier: list[tuple[int, int]]) -> list[tuple[int, int]]:
    dirs = ((1, 0), (0, 1), (-1, 0), (0, -1))
    new_frontier: set[tuple[int, int]] = set()

    for x, y in frontier:
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if not (nx in range(width) and ny in range(height)):
                continue
            if grid[ny][nx] == "#":
                continue

            new_frontier.add((nx, ny))

    return list(new_frontier)


step = 0
NUM_STEPS = 64
for _ in range(NUM_STEPS):
    step += 1

    if step & 1:  # odd
        even_frontier = process_step(odd_frontier)
        odd_count = len(even_frontier)
    else:
        odd_frontier = process_step(even_frontier)
        even_count = len(odd_frontier)

count = odd_count if NUM_STEPS & 1 else even_count
print(count)

