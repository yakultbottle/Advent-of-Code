grid: list[list[str]] = [list(string) for string in open(0).read().strip().split("\n")]

width, height = len(grid[0]), len(grid)
assert(width == height)


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


def step(num_steps: int, start: tuple[int, int]) -> int:
    odd_count, even_count = 0, 1
    odd_frontier, even_frontier = [start], []

    step = 0
    for _ in range(num_steps):
        step += 1

        if step & 1:  # odd
            even_frontier = process_step(odd_frontier)
            if odd_count == len(even_frontier):
                break
            odd_count = len(even_frontier)
        else:
            odd_frontier = process_step(even_frontier)
            if even_count == len(odd_frontier):
                break
            even_count = len(odd_frontier)

    return odd_count if num_steps & 1 else even_count


NUM_STEPS = 26501365
n = (NUM_STEPS - (width // 2)) // width

centre = (width // 2, height // 2)
odd = step(100001, centre)
even = step(100000, centre)
odd_total = odd * ((n - 1) * (n - 1))
even_total = even * (n * n)

house_steps = width - 1
house_top   = step(house_steps, (width // 2, height - 1))
house_left  = step(house_steps, (width - 1, height // 2))
house_right = step(house_steps, (0, height // 2))
house_bot   = step(house_steps, (width // 2, 0))
house_total = house_top + house_left + house_right + house_bot

triangle_steps = (width - 1) - (width // 2 + 1)
triangle_tl = step(triangle_steps, (width - 1, height - 1))
triangle_tr = step(triangle_steps, (0, height - 1))
triangle_bl = step(triangle_steps, (width - 1, 0))
triangle_br = step(triangle_steps, (0, 0))
triangle_total = n * (triangle_tl + triangle_tr + triangle_bl + triangle_br)

missing_triangle_steps = (2 * width - 1) - (width // 2 + 1)
missing_triangle_tl = step(missing_triangle_steps, (width - 1, height - 1))
missing_triangle_tr = step(missing_triangle_steps, (0, height - 1))
missing_triangle_bl = step(missing_triangle_steps, (width - 1, 0))
missing_triangle_br = step(missing_triangle_steps, (0, 0))
missing_triangle_total = (n - 1) * (missing_triangle_tl + missing_triangle_tr + missing_triangle_bl + missing_triangle_br)

total = odd_total + even_total + house_total + triangle_total + missing_triangle_total
print(total)

