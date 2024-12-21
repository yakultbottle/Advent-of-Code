import sys

def read_data() -> tuple[str,str]:
    input = sys.stdin.read().split("\n\n")
    grid = input[0]
    instructions = "".join(input[1].split("\n"))
    return (grid, instructions)

def pre_process(grid: str) -> str:
    new = []
    for c in grid:
        if c == "#":
            new.append("##")
        elif c == "O":
            new.append("[]")
        elif c == ".":
            new.append("..")
        elif c == "@":
            new.append("@.")
        else:
            new.append(c)
    return "".join(new)

def main(grid: str, instructions: str):
    grid = [list(line) for line in grid.split("\n")]
    W = len(grid[0])
    H = len(grid)

    for i in range(H):
        for j in range(W):
            if grid[i][j] == "@":
                robot = (j, i)
                break

    for i, instruction in enumerate(instructions):
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

        def check_push(here: tuple[int,int], dir: tuple[int,int], visited=None) -> bool:
            if visited is None:
                visited = set()

            x, y = here
            dx, dy = dir
            new_x = x + dx
            new_y = y + dy

            if here in visited:
                return True
            visited.add(here)

            if not (0 <= new_x < W and 0 <= new_y < H):
                return False

            tile = grid[new_y][new_x]

            if tile == ".":
                return True

            if tile == "#":
                return False

            if tile == "[":
                other_x = new_x + 1
            elif tile == "]":
                other_x = new_x - 1

            if not (0 <= other_x < W and 0 <= new_y < H):
                return False

            return check_push((new_x, new_y), dir, visited) and check_push((other_x, new_y), dir, visited)


        def push(here: tuple[int,int], dir: tuple[int,int]):
            x, y = here
            dx, dy = dir
            new_x = x + dx
            new_y = y + dy

            if not (0 <= new_x < W and 0 <= new_y < H):
                return

            tile = grid[new_y][new_x]
            if tile == ".":
                grid[y][x], grid[new_y][new_x] = grid[new_y][new_x], grid[y][x]
                return

            if tile == "[":
                other_x = new_x + 1
            elif tile == "]":
                other_x = new_x - 1

            if not (0 <= other_x < W and 0 <= new_y < H):
                return

            if grid[new_y][new_x] == "[" and dir == (1, 0):
                if check_push((other_x, new_y), dir):
                    push((other_x, new_y), dir)
                    grid[new_y][new_x], grid[new_y][other_x] = grid[new_y][other_x], grid[new_y][new_x]
                    grid[y][x], grid[new_y][new_x] = grid[new_y][new_x], grid[y][x]
                return

            if grid[new_y][new_x] == "]" and dir == (-1, 0):
                if check_push((other_x, new_y), dir):
                    push((other_x, new_y), dir)
                    grid[new_y][new_x], grid[new_y][other_x] = grid[new_y][other_x], grid[new_y][new_x]
                    grid[y][x], grid[new_y][new_x] = grid[new_y][new_x], grid[y][x]
                return

            if check_push((new_x, new_y), dir) and check_push((other_x, new_y), dir):
                push((new_x, new_y), dir)
                push((other_x, new_y), dir)
                grid[y][x], grid[new_y][new_x] = grid[new_y][new_x], grid[y][x]

        if check_push(robot, dir):
            push(robot, dir)
            robot = (new_x, new_y)
        '''
        print(instruction)
        print_grid(grid)
        '''
    return grid

def post_process(grid: list[list[str]]) -> int:
    answer = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "[":
                answer += 100 * i + j
    return answer

def print_grid(grid: list[list[str]]):
    for i in range(len(grid)):
        temp = "".join(grid[i])
        print(temp)

if __name__ == "__main__":
    grid, instructions = read_data()
    grid = pre_process(grid)
    grid = main(grid, instructions)
    print_grid(grid)
    print()
    output = post_process(grid)
    print(output)
