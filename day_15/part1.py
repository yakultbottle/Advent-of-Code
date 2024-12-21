import sys

def read_data() -> tuple[str,str]:
    input = sys.stdin.read().split("\n\n")
    grid = input[0]
    instructions = "".join(input[1].split("\n"))
    return (grid, instructions)

def main(grid: str, instructions: str):
    grid = [list(line) for line in grid.split("\n")]
    W = len(grid[0])
    H = len(grid)

    for i in range(H):
        for j in range(W):
            if grid[i][j] == "@":
                robot = (j, i)
                break

    for instruction in instructions:
        if instruction == "<":
            dir = (-1, 0)
        elif instruction == ">":
            dir = (1, 0)
        elif instruction == "^":
            dir = (0, -1)
        else:
            dir = (0, 1)

        x, y = robot
        dx, dy = dir
        new_x = x + dx
        new_y = y + dy

        def push(here: tuple[int,int], dir: tuple[int,int]) -> bool:
            x, y = here
            dx, dy = dir
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < W and 0 <= new_y < H):
                return False

            tile = grid[new_y][new_x]
            if tile == ".":
                grid[y][x], grid[new_y][new_x] = grid[new_y][new_x], grid[y][x]
                return True
            elif tile == "O":
                if push((new_x, new_y), dir):
                    grid[y][x], grid[new_y][new_x] = grid[new_y][new_x], grid[y][x]
                    return True
            return False

        if push(robot, dir):
            robot = (new_x, new_y)
    return grid

def post_process(grid: list[list[str]]) -> int:
    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "O":
                answer += 100 * i + j
    return answer

if __name__ == "__main__":
    grid, instructions = read_data()
    grid = main(grid, instructions)
    output = post_process(grid)
    print(output)
