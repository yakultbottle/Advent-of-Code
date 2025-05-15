grid = [list(row) for row in open(0).read().strip().split("\n")]

height, width = len(grid), len(grid[0])

'''
for row in grid:
    print(''.join(row))
print()
'''

for i in range(1, height):
    for j in range(width):
        if grid[i][j] != "O":
            continue

        curr = i
        while curr > 0 and grid[curr - 1][j] == ".":
            grid[curr][j], grid[curr - 1][j] = grid[curr - 1][j], grid[curr][j]
            curr -= 1

'''
for row in grid:
    print(''.join(row))
'''

load = 0
for i in range(height):
    for j in range(width):
        if grid[i][j] != "O":
            continue
        
        load += (height - i)
print(load)

