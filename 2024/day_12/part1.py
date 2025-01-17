import sys

def read_data() -> list[list[str]]:
    return [list(line.strip()) for line in sys.stdin]

def dfs(grid: list[list[str]], visited: list[list[bool]], pos: tuple[int,int], price: tuple[int,int]) -> tuple[int,int]:
    neighbours = 0
    area = 0
    perimeter = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for direction in directions:
        dx, dy = direction
        x, y = pos
        newX, newY = x + dx, y + dy

        if not (0 <= newX < len(grid[0]) and 0 <= newY < len(grid)):
            continue

        if grid[newY][newX] == grid[y][x]:
            neighbours += 1
            if not visited[newY][newX]:
                visited[newY][newX] = True
                new_area, new_perimeter = dfs(grid, visited, (newX, newY), price)
                area += new_area
                perimeter += new_perimeter

    return (area + 1, perimeter + 4 - neighbours)

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
        area, perimeter = plot
        res += area * perimeter
    return res

if __name__ == "__main__":
    grid = read_data()
    output = main(grid)
    output = post_process(output)
    print(output)
