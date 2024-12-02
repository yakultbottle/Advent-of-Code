from typing import List
import sys

def read_data() -> List[List[int]]:
    input_lines = sys.stdin.read().strip().splitlines()

    data = []
    for line in input_lines:
        data.append([int(x) for x in line.split()])

    return data

def is_safe_report(report: List[int]) -> bool:
    is_increasing = report[1] > report[0]

    for i in range(1, len(report)):
        diff = report[i] - report[i - 1] if is_increasing else report[i - 1] - report[i]
        if diff < 1 or diff > 3:
            return False

    return True

def main(input: List[List[int]]) -> int:
    count = 0

    for line in input:
        if is_safe_report(line):
            count += 1
        else:
            for i in range(len(line)):
                line_copy = line.copy()
                line_copy.pop(i)
                if is_safe_report(line_copy):
                    count += 1
                    break

    return count

if __name__ == "__main__":
    input = read_data()
    ans = main(input)
    print(ans)
