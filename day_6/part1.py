import sys

def read_data() -> list[list[str]]:
    input = sys.stdin.readlines()
    map = [list(line.strip()) for line in input]
    return map

def print_board(board: list[list[str]]):
    for row in board:
        output = ""
        for tile in row:
            output += tile
        print(output)

def main(map: list[list[str]]) -> int:
    guard = (0, 0)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == '^':
                map[i][j] = "X"
                guard = (j, i)

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    curr_direction = 0

    finish = False
    while not finish:
        x, y = guard
        # print(guard)
        # for dx, dy in directions:
        while True:
            dx, dy = directions[curr_direction]
            newX = x + dx
            newY = y + dy

            if not (0 <= newX and newX < len(map[0]) and 0 <= newY and newY < len(map)):
                finish = True
                break

            if map[newY][newX] != "#":
                map[newY][newX] = "X"
                guard = (newX, newY)
                break
            else:
                curr_direction = (curr_direction + 1) % 4

        # print_board(map)
        # print()

    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == "X":
                count += 1

    return count

if __name__ == "__main__":
    map = read_data()
    output = main(map)
    print(output)
