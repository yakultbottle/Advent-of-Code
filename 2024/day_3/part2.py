from typing import List
import sys
import re

def read_data() -> str:
    input = sys.stdin.read().strip()
    return handle_dos(input)

def handle_dos(input: str) -> str:
    do_str = r"do\(\)"
    dont_str = r"don't\(\)"
    instruction_regex = re.compile(f"{do_str}|{dont_str}")

    sections = instruction_regex.split(input)
    instructions = instruction_regex.findall(input)

    enabled = True
    result = []

    for section, instruction in zip(sections, instructions + [None]):
        if enabled:
            result.append(section)
        if instruction == "do()":
            enabled = True
        elif instruction == "don't()":
            enabled = False

    return ''.join(result)

def process_data(input: str) -> List[str]:
    mul_regex = re.compile(r"mul\(\d+,\d+\)")
    return mul_regex.findall(input)

def main(muls: List[str]) -> int:
    digit = re.compile(r"\d+")
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
