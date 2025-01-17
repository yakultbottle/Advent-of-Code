import sys

def read_data() -> list[list[int]]:
    input = sys.stdin.readlines()
    map = [[int(char) for char in string.strip()] for string in input]
    return map

def count_trails(map: list[list[int]], curr: int, x: int, y: int) -> int:
    if curr == 9:
        return 1

    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    count = 0

    for direction in directions:
        dx, dy = direction
        newX, newY = x + dx, y + dy

        if not (0 <= newX < len(map[0]) and 0 <= newY < len(map)):
            continue

        if map[newY][newX] == curr + 1:
            count += count_trails(map, curr + 1, newX, newY)
    return count

def main(map: list[list[int]]) -> int:
    count = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 0:
                count += count_trails(map, 0, j, i)

    return count

if __name__ == "__main__":
    map = read_data()
    output = main(map)
    print(output)
