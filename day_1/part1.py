from typing import List
import sys

def read_data() -> List[tuple[int,int]]:
    input_lines = sys.stdin.read().strip().splitlines()

    data = []
    for line in input_lines:
        pair = tuple(map(int, line.split()))
        data.append(pair)

    return data

def sort_input(input: List[tuple[int,int]]) -> List[tuple[int,int]]:
    list1, list2 = zip(*input)
    list1 = sorted(list1)
    list2 = sorted(list2)
    return list(zip(list1,list2))

def main(input: List[tuple[int,int]]) -> int:
    difference = 0
    for line in input:
        first, second = line # unpacking tuple
        difference += abs(first - second)
    return difference

if __name__ == "__main__":
    input = read_data()
    input = sort_input(input)
    difference = main(input)
    print(difference)
