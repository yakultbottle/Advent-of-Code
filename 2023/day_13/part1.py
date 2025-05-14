input = open(0).read().strip()

def reflection(grid: list[list[str]]) -> int:
    rows = len(grid)
    for row in range(rows - 1):
        top, bottom = row, row + 1
        while top >= 0 and bottom < rows and "".join(grid[top]) == "".join(grid[bottom]):
            top -= 1
            bottom += 1
        if top == -1 or bottom == rows:
            return row + 1
    return -1

count = 0
for block in input.split("\n\n"):
    grid = [[char for char in line] for line in block.split("\n")]

    horizontal_lines = reflection(grid)
    if horizontal_lines >= 0:
        count += horizontal_lines * 100
    else:
        vertical_lines = reflection(list(zip(*grid)))
        count += vertical_lines

print(count)

