import sys
from collections import defaultdict

def read_data() -> list[list[str]]:
    input = sys.stdin.readlines()
    trimmed = [list(line.strip()) for line in input]
    return trimmed

def in_bounds(coord: tuple[int,int], map: list[list[str]]) -> bool:
    return 0 <= coord[0] and coord[0] < len(map[0]) and 0 <= coord[1] and coord[1] < len(map)

def main(map: list[list[str]]):
    antinodes = set()
    nodes = defaultdict(list)
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == ".":
                continue

            if map[i][j] in nodes:
                for other_node in nodes[map[i][j]]:
                    x, y = other_node
                    dx = j - x
                    dy = i - y
                    first = (x - dx, y - dy)
                    second = (j + dx, i + dy)
                    while in_bounds(first, map):
                        antinodes.add(first)
                        first = (first[0] - dx, first[1] - dy)
                    while in_bounds(second, map):
                        antinodes.add(second)
                        second = (second[0] + dx, second[1] + dy)
            nodes[map[i][j]].append((j, i))

    for antennas in nodes:
        for antenna in nodes[antennas]:
            antinodes.add(antenna)
    return len(antinodes)

if __name__ == "__main__":
    input = read_data()
    output = main(input)
    print(output)