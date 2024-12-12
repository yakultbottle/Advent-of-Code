import sys

def read_data() -> list[list[str]]:
    return [list(line.strip()) for line in sys.stdin]

def dfs(grid: list[list[str]], visited: list[list[bool]], pos: tuple[int,int], price: tuple[int,int]) -> tuple[int,int]:
    prev_is_neighbour = False
    area = 0
    sides = 0

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 0)]
    diagonals = [(0, 0), (1, 1), (-1, 1), (-1, -1), (1, -1)]
    for i, direction in enumerate(directions):
        dx, dy = direction
        x, y = pos
        newX, newY = x + dx, y + dy

        if not (0 <= newX < len(grid[0]) and 0 <= newY < len(grid)):
            if not prev_is_neighbour and i != 0:
                sides += 1
            prev_is_neighbour = False
            continue

        if grid[newY][newX] == grid[y][x]:
            if prev_is_neighbour:
                dx2, dy2 = diagonals[i]
                diagX, diagY = x + dx2, y + dy2
                if grid[diagY][diagX] != grid[y][x]:
                    sides += 1
            prev_is_neighbour = True

            if not visited[newY][newX]:
                visited[newY][newX] = True
                new_area, new_sides = dfs(grid, visited, (newX, newY), price)
                area += new_area
                sides += new_sides
        else:
            if i == 0:
                continue
            if not prev_is_neighbour:
                sides += 1
            prev_is_neighbour = False

    return (area + 1, sides)

def main(grid: list[list[str]]) -> list[tuple[int,int]]:
    visited = [[False for _ in grid[0]] for _ in grid]
    total = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if visited[row][col]:
                continue
            
            visited[row][col] = True
            price = dfs(grid, visited, (col, row), (0, 0))
            total.append(price)

    return total

def post_process(output: list[tuple[int,int]]) -> int:
    res = 0
    for plot in output:
        area, sides = plot
        res += area * sides
    return res

if __name__ == "__main__":
    grid = read_data()
    output = main(grid)
    output = post_process(output)
    print(output)
