input = open(0).read().strip()

def reflection(grid: list[list[str]], ignore: int) -> int:
    rows = len(grid)
    for row in range(rows - 1):
        top, bottom = row, row + 1
        while top >= 0 and bottom < rows and "".join(grid[top]) == "".join(grid[bottom]):
            top -= 1
            bottom += 1
        if (top == -1 or bottom == rows) and (ignore < 0 or ignore != row + 1):
            return row + 1
    return -1

'''
def find_reflect(grid: list[list[str]], ignore: int) -> int:
    horizontal_lines = reflection(grid, ignore)
    if horizontal_lines >= 0:
        initial = horizontal_lines * 100
    else:
        vertical_lines = reflection(list(zip(*grid)), ignore)
        initial = vertical_lines

    return initial
'''

def find_smudge(grid: list[list[str]]) -> int:
    initial_hori = reflection(grid, -1)
    initial_vert = reflection(list(zip(*grid)), -1) if initial_hori < 0 else -1

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j] = "#" if grid[i][j] == "." else "."

            new_hori = reflection(grid, initial_hori)
            new_vert = reflection(list(zip(*grid)), initial_vert)

            if new_hori > 0 and new_hori != initial_hori:
                return new_hori * 100
            elif new_vert > 0 and new_vert != initial_vert:
                return new_vert

            grid[i][j] = "#" if grid[i][j] == "." else "."

    print("NOOOOOO")
    # print(initial)
    for row in grid:
        print(''.join(row))
    print()
    return -1

count = 0
for block in input.split("\n\n"):
    grid = [[char for char in line] for line in block.split("\n")]

    count += find_smudge(grid)

print(count)

