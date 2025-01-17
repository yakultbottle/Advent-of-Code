from typing import List
import sys
import re

def read_data() -> str:
    input = sys.stdin.read().strip()
    return input

def process_data(input: str) -> List[str]:
    mul_regex = re.compile("mul\(\d+,\d+\)")
    return mul_regex.findall(input)

def main(muls: List[str]) -> int:
    digit = re.compile("\d+")
    res = 0
    for mul in muls:
        nums = digit.findall(mul)
        nums = [int(num) for num in nums]
        res += nums[0] * nums[1]
    return res

if __name__ == "__main__":
    input = read_data()
    processed_input = process_data(input)
    output = main(processed_input)
    print(output)
