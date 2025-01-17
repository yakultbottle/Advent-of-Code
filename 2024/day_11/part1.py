import sys

def read_data() -> tuple[int,list[int]]:
    input = sys.stdin.readlines()
    n = int(input[0].strip())
    stones = [int(stone) for stone in input[1].strip().split(" ")]
    return (n, stones)

def main(n: int, stones: list[int]):
    for i in range(n):
        j = 0
        while j < len(stones):
            if stones[j] == 0:
                stones[j] = 1
                j += 1
                continue

            stone_str = str(stones[j])
            length = len(stone_str)
            if length % 2 == 0:
                one = int(stone_str[0:length // 2])
                two = int(stone_str[(length // 2):length])
                stones.pop(j)
                stones.insert(j, two)
                stones.insert(j, one)
                j += 2
            else:
                stones[j] = stones[j] * 2024
                j += 1
    return stones

if __name__ == "__main__":
    n, stones = read_data()
    output = main(n, stones)
    print(len(output))
