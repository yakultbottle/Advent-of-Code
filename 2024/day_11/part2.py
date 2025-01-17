import sys
import math

def read_data() -> tuple[int,list[int]]:
    input = sys.stdin.readlines()
    n = int(input[0].strip())
    stones = [int(stone) for stone in input[1].strip().split(" ")]
    return (n, stones)

def split_number(stone: int) -> tuple[int,int]:
    num_digits = math.floor(math.log10(stone)) + 1
    
    half_digits = num_digits // 2
    divisor = 10 ** half_digits

    left = stone // divisor
    right = stone % divisor
    return left, right

memo = {}
def calc_len(n: int, stone: int) -> int:
    if (n, stone) in memo:
        return memo[(n, stone)]

    if n <= 0:
        return 1

    if stone == 0:
        memo[(n, stone)] = calc_len(n - 1, 1)
        return memo[(n, stone)]

    num_digits = math.floor(math.log10(stone)) + 1
    if num_digits % 2 == 0:
        one, two = split_number(stone)
        memo[(n - 1, one)] = calc_len(n - 1, one)
        memo[(n - 1, two)] = calc_len(n - 1, two)
        memo[(n, stone)] = memo[(n - 1, one)] + memo[(n - 1, two)]
        return memo[(n, stone)]
    else:
        memo[(n, stone)] = calc_len(n - 1, stone * 2024)
        return memo[(n, stone)]

def main(n: int, stones: list[int]) -> int:
    count = 0
    for stone in stones:
        count += calc_len(n, stone)
    return count

if __name__ == "__main__":
    n, stones = read_data()
    output = main(n, stones)
    print(output)
