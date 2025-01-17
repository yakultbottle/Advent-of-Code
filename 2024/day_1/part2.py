from typing import List
import sys

def read_data() -> List[tuple[int,int]]:
    input_lines = sys.stdin.read().strip().splitlines()

    data = []
    for line in input_lines:
        pair = tuple(map(int, line.split()))
        data.append(pair)

    return data

def main(input: List[tuple[int,int]]) -> int:
    list1, list2 = zip(*input)
    freq = {}
    for item in list2:
        freq[item] = freq.get(item, 0) + 1
    similarity = 0
    for item in list1:
        similarity += item * freq.get(item, 0)
    return similarity

if __name__ == "__main__":
    input = read_data()
    difference = main(input)
    print(difference)
